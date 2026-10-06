from flask import Blueprint, jsonify, request
from datetime import datetime
from app.models import Trip
from app import db

main = Blueprint("main", __name__)


@main.route("/health", methods=["GET"])
def health():
    return jsonify(
        {
            "status": "ok"
        }
    ), 200


@main.route("/api/v1/trips", methods=["POST"])
def create_trip():
    data = request.get_json()
    try:
        start_date = datetime.strptime(data["start_date"], "%Y-%m-%d").date()
        end_date = datetime.strptime(data["end_date"], "%Y-%m-%d").date()
    except ValueError:
        return jsonify({
            "error": "Invalid date format follow (YYYY-MM-DD)"
        }), 400
    if end_date <= start_date:
        return jsonify({
            "error": "End date must be after the start date"
        }), 400
    if data["budget"] <= 0:
        return jsonify({
            "error": "Budget must be positive"
        }), 400
    if data["max_travelers"] <= 0:
        return jsonify({
            "error": "Maximum travelers must be positive"
        }), 400

    trip = Trip(
        destination=data["destination"],
        start_date=start_date,
        end_date=end_date,
        budget=data["budget"],
        max_travelers=data["max_travelers"],
        status="PLANNED"
    )

    db.session.add(trip)
    db.session.commit()

    return jsonify({
        "id": trip.id,
        "destination": trip.destination,
        "status": trip.status
    }), 201


@main.route("/api/v1/trips", methods=["GET"])
def get_trips():
    trips = Trip.query.all()
    result = []

    for trip in trips:
        result.append({
            "id": trip.id,
            "destination": trip.destination,
            "start_date": str(trip.start_date),
            "end_date": str(trip.end_date),
            "budget": trip.budget,
            "max_travelers": trip.max_travelers,
            "status": trip.status
        })

    return jsonify(result), 200


@main.route("/api/v1/trips/<int:trip_id>", methods=["Get"])
def get_trip(trip_id):
    trip = Trip.query.get(trip_id)

    if not trip:
        return jsonify({
            "error": "Trip not Found"
        }), 404

    return jsonify({
        "id": trip.id,
        "destination": trip.destination,
        "start_date": str(trip.start_date),
        "end_date": str(trip.end_date),
        "budget": trip.budget,
        "max_travelers": trip.max_travelers,
        "status": trip.status
    }), 200


@main.route("/api/v1/trips", methods=["PUT"])
def update_trip(trip_id):
    trip = Trip.query.get(trip_id)

    if not trip:
        return jsonify({
            "error": "Trip Not Found"
        }), 404

    if trip.status != "PLANNED":
        return jsonify({
            "error": "Only Planned trips can be edited"
        }), 409

    data = request.get_json()

    if "destination" in data:
        trip.destination = data["destination"]
    if "budget" in data:
        if data["budget"] <= 0:
            return jsonify({
                "error": "Invalid budget"
            }), 400
        trip.budget = data["budget"]

    db.session.commit()
    return jsonify({
        "message": "Trip updated"
    }), 200


@main.route("/api/v1/trips", methods=["DELETE"])
def delete_trip(trip_id):
    trip = Trip.query.get(trip_id)
    if not trip:
        return jsonify({
            "error": "Trip Not Found"
        }), 404

    db.session.delete(trip)
    db.session.commit()
    return jsonify({
        "message": "Trip deleted"
    }), 200
