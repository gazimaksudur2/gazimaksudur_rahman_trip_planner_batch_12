from app.exceptions.business_exception import BusinessException
from app.exceptions.not_found_exception import NotFoundException
from app.models import Trip, Expense
from app.extensions import db


def add_expense(trip_id, data):
    trip = Trip.query.get(trip_id)

    if not trip:
        raise NotFoundException("Trip Not Found")

    if trip.status not in ["PLANNED", "ONGOING"]:
        raise BusinessException("Expenses can only be added to planned trips")

    current_expenses = sum(float(expense.amount) for expense in trip.expenses)

    if float(current_expenses + data["amount"]) > float(trip.budget):
        raise BusinessException("Total expenses cannot exceed the trip budget")

    title = data["title"]
    amount = data["amount"]

    if not title or not amount:
        raise BusinessException("Title and Amount are required")

    expense = Expense(title=title, amount=amount, trip_id=trip.id)

    db.session.add(expense)
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise BusinessException("Failed to add expense")

    return expense


def get_trip_expenses(trip_id):
    return Expense.query.filter_by(trip_id=trip_id).all()
