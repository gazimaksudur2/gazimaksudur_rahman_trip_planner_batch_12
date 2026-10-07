from app.extensions import db
from app.models import Trip

from app.validators.trip_validator import validate_trip_data


def create_trip(data):
    start_date, end_date = validate_trip_data(data)
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

    return trip


def get_all_trips():
    return Trip.query.all()


def get_trip_by_id(trip_id):
    return Trip.query.get(trip_id)


def update_trip(trip_id, data):
    trip = Trip.query.get(trip_id)
    if not trip:
        return None
        
    if trip.status != "PLANNED":
        raise ValueError("Only planned trips can be edited")

    if "destination" in data:
        trip.destination = data["destination"]

    if "budget" in data:
        if data["budget"] <= 0:
            raise ValueError("Budget must be greater than zero")
        trip.budget = data["budget"]

    db.session.commit()
    return trip


def delete_trip(trip_id):
    trip = Trip.query.get(trip_id)

    if not trip:
        return None

    db.session.delete(trip)
    db.session.commit()
    return trip
