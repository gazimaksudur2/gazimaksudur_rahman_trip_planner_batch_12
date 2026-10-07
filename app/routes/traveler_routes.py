from flask import Blueprint, request, jsonify
from app.services import traveler_service

traveler_bp = Blueprint("traveler", __name__, url_prefix="/api/v1")


@traveler_bp.route("/trips/<int:trip_id>/travelers", methods=["POST"])
def add_traveler(trip_id):
    try:
        traveler = traveler_service.add_traveler(
            trip_id,
            data=request.get_json()
        )

        return jsonify({
            "id": traveler.id,
            "user_id": traveler.user_id,
            "name": traveler.user.name,
            "email": traveler.user.email,
            "trip_id": traveler.trip_id,
            "joined_at": str(traveler.joined_at)
        }), 201

    except ValueError as error:

        return jsonify({
            "error": str(error)
        }), 400


@traveler_bp.route("/trips/<int:trip_id>/travelers/<int:traveler_id>",
                   methods=["DELETE"])
def remove_traveler(trip_id, traveler_id):
    try:
        traveler_service.remove_traveler(trip_id, traveler_id)
        return jsonify({
            "message": f"Traveler {traveler_id} removed from {trip_id}"
        }), 200

    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 404
