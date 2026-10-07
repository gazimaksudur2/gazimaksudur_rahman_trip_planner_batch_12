from app.extensions import db
from app.models import Trip

from app.validators import status_validator


def update_trip_status(trip_id, new_status):
    trip = Trip.query.get(trip_id)

    if not trip:
        raise ValueError("Trip not found")

    status_validator.validate_status_transition(
        trip.status,
        new_status
    )

    trip.status = new_status

    db.session.commit()

    return trip
