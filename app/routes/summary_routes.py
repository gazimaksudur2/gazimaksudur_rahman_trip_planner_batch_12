from flask import Blueprint, jsonify
from app.exceptions.business_exception import BusinessException
from app.services import summary_service


summary_bp = Blueprint("summary", __name__, url_prefix="/api/v1")


@summary_bp.route("/trips/<int:trip_id>/summary", methods=["GET"])
def get_trip_summary(trip_id):
    try:
        summary = summary_service.get_trip_summary(trip_id)
        return jsonify(summary), 200
    except BusinessException as error:
        return error, 400
