from app.models import Trip, Expense
from app.extensions import db


def add_expense(trip_id, data):
    trip = Trip.query.get(trip_id)

    if not trip:
        raise ValueError("Trip Not Found")

    if trip.status not in ["PLANNED", "ONGOING"]:
        raise ValueError("Expenses can only be added to planned trips")

    current_expenses = sum(expense.amount for expense in trip.expenses)

    if float(current_expenses + data["amount"]) > float(trip.budget):
        raise ValueError("Total expenses cannot exceed the trip budget")

    title = data["title"]
    amount = data["amount"]

    if not title or not amount:
        raise ValueError("Title and Amount are required")

    expense = Expense(title=title, amount=amount, trip_id=trip.id)

    db.session.add(expense)
    db.session.commit()

    return expense


def get_trip_expenses(trip_id):
    return Expense.query.filter_by(trip_id=trip_id).all()
