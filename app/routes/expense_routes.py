from flask import Blueprint, request, jsonify
from app.exceptions.business_exception import BusinessException
from app.services import expense_service


expense_bp = Blueprint("expenses", __name__, url_prefix="/api/v1")


@expense_bp.route("/trips/<int:trip_id>/expenses", methods=["POST"])
def add_expense(trip_id):
    data = request.get_json()
    try:
        expense = expense_service.add_expense(trip_id, data)
        return jsonify({
            "id": expense.id,
            "trip_id": expense.trip_id,
            "title": expense.title,
            "amount": expense.amount
        }), 201
    except BusinessException as error:
        return error, 400
