from flask import Blueprint, request, jsonify
from app.services import trip_service
from app.utils.serializer import trip_to_dict


trip_bp = Blueprint("trips", __name__, url_prefix="/api/v1")


@trip_bp.route("/trips", methods=["POST"])
def create_trip():
    try:
        trip = trip_service.create_trip(
            request.get_json()
        )
        return jsonify(trip_to_dict(trip)), 201
    
    except ValueError as error:

        return jsonify({
            "error": str(error)
        }), 400


@trip_bp.route("/trips", methods=["GET"])
def list_trips():
    trips = trip_service.get_all_trips()

    return jsonify(
        [trip_to_dict(trip) for trip in trips]
    ), 200


@trip_bp.route("/trips/<int:trip_id>", methods=["GET"])
def get_trip(trip_id):
    trip = trip_service.get_trip_by_id(trip_id)
    if not trip:
        return jsonify({
            "error": "Trip not found"
        }), 404

    return jsonify(
        trip_to_dict(trip)
    ), 200


@trip_bp.route("/trips/<int:trip_id>", methods=["PUT"])
def update_trip(trip_id):
    try:
        trip = trip_service.update_trip(
            trip_id,
            request.get_json()
        )

        if not trip:
            return jsonify({
                "error": "Trip not found"
            }), 404

        return jsonify(
            trip_to_dict(trip)
        ), 200
    
    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 409


@trip_bp.route("/trips/<int:trip_id>", methods=["DELETE"])
def delete_trip(trip_id):
    trip = trip_service.delete_trip(trip_id)

    if not trip:
        return jsonify({
            "error": "Trip not found"
        }), 404

    return jsonify({
        "message": "Trip deleted"
    }), 200