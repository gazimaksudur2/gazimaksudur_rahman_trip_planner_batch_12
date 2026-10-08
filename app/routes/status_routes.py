from flask import Blueprint, request, jsonify
from app.exceptions.business_exception import BusinessException
from app.services import status_service

status_bp = Blueprint("status", __name__, url_prefix="/api/v1")


@status_bp.route("/trips/<int:trip_id>/status", methods=["PATCH"])
def update_status(trip_id):
    try:
        data = request.get_json()
        trip = status_service.update_trip_status(trip_id, data["status"])

        return jsonify({
            "trip_id": trip_id,
            "status": trip.status
        }), 200
    except BusinessException as error:
        return error, 400
