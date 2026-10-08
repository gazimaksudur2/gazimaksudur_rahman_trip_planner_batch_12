from app.exceptions.not_found_exception import NotFoundException
from app.models import Trip


def get_trip_summary(trip_id):
    trip = Trip.query.get(trip_id)
    if not trip:
        raise NotFoundException("Trip Not Found")

    traveler_count = len(trip.travelers)
    total_expenses = sum(float(expense.amount) for expense in trip.expenses)
    remaining_budget = max(0, trip.budget - total_expenses)
    available_seats = trip.max_travelers - traveler_count

    return {
        "trip_id": trip.id,
        "destination": trip.destination,
        "status": trip.status,
        "number_of_travelers": traveler_count,
        "total_expenses": total_expenses,
        "remaining_budget": remaining_budget,
        "available_seats": available_seats
    }
