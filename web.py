from flask import Flask, jsonify, request

from app import calculate

app = Flask(__name__, static_folder="static")
app.config["MAX_CONTENT_LENGTH"] = 16000


@app.get("/")
def index():
    return app.send_static_file("index.html")


@app.post("/api/calculate")
def calculate_trip():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify(error="Please submit valid trip details."), 400

    try:
        return jsonify(calculate(data))
    except (ValueError, TypeError, KeyError, OverflowError) as error:
        return jsonify(error=str(error)), 400
    except Exception:
        app.logger.exception("Trip calculation failed")
        return jsonify(error="Unable to calculate this trip. Try again."), 500