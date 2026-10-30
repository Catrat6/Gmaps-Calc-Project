import json
import os
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parent
OFFICE = "N5806 Co Rd M, Plymouth, WI 53073"


def load_env():
    path = ROOT / ".env"
    if path.exists():
        for line in path.read_text().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


load_env()


def route(origin, destination):

    key = os.getenv("GOOGLE_MAPS_API_KEY")

    if not key:
        raise ValueError(
            "Add GOOGLE_MAPS_API_KEY to the .env file, or select manual mileage."
        )
    req = Request(
        "https://routes.googleapis.com/directions/v2:computeRoutes",
        data=json.dumps(
            {
                "origin": {"address": origin},
                "destination": {"address": destination},
                "travelMode": "DRIVE",
            }
        ).encode(),
        headers={
            "Content-Type": "application/json",
            "X-Goog-Api-Key": key,
            "X-Goog-FieldMask": "routes.distanceMeters,routes.duration",
        },
    )
    try:
        with urlopen(req, timeout=20) as response:
            routes = json.load(response).get("routes", [])
        if not routes:
            raise ValueError("No driving route found. Check both addresses.")
        r = routes[0]
        return {
            "miles": round(r["distanceMeters"] / 1609.344),
            "minutes": round(float(r["duration"].rstrip("s")) / 60),
        }
    except HTTPError:
        raise ValueError(
            "Google Maps rejected the request. Check the API key, Routes API access, and billing."
        ) from None
    except (URLError, TimeoutError):
        raise ValueError(
            "Google Maps could not be reached. Try again or use manual mileage."
        ) from None


def number(data, key, maximum=100000):
    value = float(data.get(key, 0))
    if not 0 <= value <= maximum:
        raise ValueError(f'{key.replace("_", " ")} must be between 0 and {maximum}.')
    return value


def calculate(data):
    legs = number(data, "legs", 100)
    wait = number(data, "wait_minutes")
    extra = number(data, "extra_charge")

    if legs < 1 or legs != int(legs):
        raise ValueError("Legs must be a whole number of at least 1.")
    if wait % 30:
        raise ValueError("Wait time must be in 30-minute intervals.")
    for key in ("round_trip", "after_hours"):
        if not isinstance(data.get(key), bool):
            raise ValueError("Invalid trip option.")
    double = 2 if data["round_trip"] else 1
    if data.get("mode") == "manual":
        trip = {
            "miles": number(data, "loaded_miles"),
            "minutes": number(data, "loaded_minutes"),
        }
        pickup = {
            "miles": number(data, "pickup_miles"),
            "minutes": number(data, "pickup_minutes"),
        }
        dropoff = {
            "miles": number(data, "dropoff_miles"),
            "minutes": number(data, "dropoff_minutes"),
        }
    elif data.get("mode") == "google":
        origin, destination = (
            str(data.get("pickup", "")).strip(),
            str(data.get("dropoff", "")).strip(),
        )
        if not origin or not destination:
            raise ValueError("Enter pickup and drop-off addresses.")
        cache = {}

        def get(a, b):
            if (a, b) not in cache:
                cache[a, b] = route(a, b)
            return cache[a, b]

        trip = get(origin, destination)
        pickup = get(OFFICE, origin)
        dropoff = get(destination, OFFICE) if double == 1 else get(origin, OFFICE)
    else:
        raise ValueError("Choose Google Maps or manual mileage.")

    loaded = trip["miles"] * double
    unloaded = sum(r["miles"] for r in (pickup, dropoff) if r["miles"] > 20)
    breakdown = {
        "Base fare": 35 * legs,
        "Loaded mileage": loaded * 2.5,
        "Unloaded mileage": unloaded * 1.5,
        "Wait time": wait / 30 * 15,
        "After hours": 20 if data["after_hours"] else 0,
        "Extra charge": extra,
    }
    subtotal = sum(breakdown.values())
    breakdown["4% fee"] = round(subtotal * 0.04, 2)
    total = round(subtotal * 1.04, 2)
    actual_miles = loaded + pickup["miles"] + dropoff["miles"]
    minutes = (
        trip["minutes"] * double
        + pickup["minutes"]
        + dropoff["minutes"]
        + wait
        + 10 * legs
    )
    operating = {
        "Fuel": round(actual_miles / 18 * 3.75, 2),
        "Driver pay": round(minutes / 60 * 20, 2),
        "Vehicle wear": round(actual_miles * 0.2, 2),
    }
    cost = round(sum(operating.values()), 2)
    return dict(
        total=total,
        operating=cost,
        profit=round(total - cost, 2),
        breakdown=breakdown,
        operating_breakdown=operating,
        loaded_miles=loaded,
        unloaded_miles=unloaded,
        total_miles=actual_miles,
        total_minutes=minutes,
    )


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT / "static"), **kwargs)

    def do_POST(self):
        if self.path != "/api/calculate":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            if not 0 < length <= 16000:
                raise ValueError("Invalid request size.")
            data = json.loads(self.rfile.read(length))
            if not isinstance(data, dict):
                raise ValueError("Invalid request.")
            result, status = calculate(data), 200
        except (ValueError, TypeError, KeyError, OverflowError) as exc:
            result, status = {"error": str(exc) or "Please check your inputs."}, 400
        except Exception:
            result, status = {
                "error": "The calculation could not finish. Please try again."
            }, 502
        payload = json.dumps(result, allow_nan=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format, *args):
        pass

    if __name__ == "__main__":
        print("Trip calculator: http://127.0.0.1:8000", flush=True)
        ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
