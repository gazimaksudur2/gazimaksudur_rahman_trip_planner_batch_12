from app.exceptions.business_exception import BusinessException
from app.exceptions.not_found_exception import NotFoundException
from app.extensions import db
from app.models import Trip

from app.validators import status_validator


def update_trip_status(trip_id, new_status):
    trip = Trip.query.get(trip_id)

    if not trip:
        raise NotFoundException("Trip not found")

    status_validator.validate_status_transition(
        trip.status,
        new_status
    )

    trip.status = new_status

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise BusinessException("Failed to update trip status")

    return trip
