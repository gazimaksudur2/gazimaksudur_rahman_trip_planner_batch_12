from app.exceptions.not_found_exception import NotFoundException
from app.exceptions.business_exception import BusinessException
from app.extensions import db
from app.models import Trip

from app.validators.trip_validator import validate_trip_data


def create_trip(data):
    start_date, end_date = validate_trip_data(data)
    trip = Trip(
        destination=data["destination"],
        start_date=start_date,
        end_date=end_date,
        budget=float(data["budget"]),
        max_travelers=int(data["max_travelers"]),
        status="PLANNED"
    )

    db.session.add(trip)
    db.session.commit()

    return trip


def get_all_trips():
    return Trip.query.all()


def get_trip_by_id(trip_id):
    trip = Trip.query.get(trip_id)
    if not trip:
        raise NotFoundException("Trip not found")
    return trip


def update_trip(trip_id, data):
    trip = Trip.query.get(trip_id)
    if not trip:
        raise NotFoundException("Trip not found")

    if trip.status != "PLANNED":
        raise BusinessException("Only planned trips can be edited")

    if "destination" in data:
        if not str(data["destination"]).strip():
            raise BusinessException("Destination cannot be empty")
        trip.destination = data["destination"]

    if "budget" in data:
        try:
            budget = float(data["budget"])
        except (ValueError, TypeError):
            raise BusinessException("Budget must be a valid number")
        if budget <= 0:
            raise BusinessException("Budget must be greater than zero")
        trip.budget = budget

    db.session.commit()
    return trip


def delete_trip(trip_id):
    trip = Trip.query.get(trip_id)

    if not trip:
        raise NotFoundException("Trip not found")

    if trip.status != "PLANNED":
        raise BusinessException("Only planned trips can be deleted")

    db.session.delete(trip)
    db.session.commit()
    return trip
