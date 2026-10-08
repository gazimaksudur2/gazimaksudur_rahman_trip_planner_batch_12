from app.exceptions.business_exception import BusinessException
from app.exceptions.not_found_exception import NotFoundException
from app.models import Trip, Traveler, User
from app.validators import traveler_validator
from app.extensions import db


def add_traveler(trip_id, data):
    traveler_validator.validate_traveler_data(data)
    trip = Trip.query.get(trip_id)

    if not trip:
        raise NotFoundException("Trip Not Found")

    if trip.status != "PLANNED":
        raise BusinessException("Travelers can only be added to planned trips")

    if len(trip.travelers) >= int(trip.max_travelers):
        raise BusinessException("Maximum travelers limit reached")

    email = data["email"]
    name = data["name"]
    user = User.query.filter_by(email=email).first()

    if not user:
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.flush()

    existing = Traveler.query.filter_by(
        user_id=user.id,
        trip_id=trip.id
    ).first()

    if existing:
        raise BusinessException("Traveler already joined to this trip")

    if has_overlapping_trip(user.id, trip):
        raise BusinessException("Traveler has overlapping trip")

    traveler = Traveler(user_id=user.id, trip_id=trip.id)

    try:
        db.session.add(traveler)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise BusinessException("Failed to add traveler")

    return traveler


def remove_traveler(trip_id, traveler_id):
    traveler = Traveler.query.filter_by(
        id=traveler_id,
        trip_id=trip_id
    ).first()

    if not traveler:
        raise NotFoundException("Traveler Not Found")

    db.session.delete(traveler)
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise BusinessException("Failed to remove traveler")
    return traveler


def has_overlapping_trip(user_id, new_trip):
    existing_memberships = Traveler.query.filter_by(user_id=user_id).all()

    for membership in existing_memberships:
        existing_trip = membership.trip

        if (existing_trip.start_date <= new_trip.end_date and
           new_trip.start_date <= existing_trip.end_date):
            return True

    return False
