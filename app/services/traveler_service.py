from app.models import Trip, Traveler, User
from app.validators import traveler_validator
from app.extensions import db


def add_traveler(trip_id, data):
    traveler_validator.validate_traveler_data(data)
    trip = Trip.query.get(trip_id)

    if not trip:
        raise ValueError("Trip Not Found")

    if trip.status != "PLANNED":
        raise ValueError("Travelers can only join planned trips")

    if len(trip.travelers) >= int(trip.max_travelers):
        raise ValueError("Maximum travelers limit reached")

    email = data["email"]
    name = data["name"]

    if not name or not email:
        raise ValueError("Name and Email are required")

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
        raise ValueError("Traveler already joined to this trip")

    if has_overlapping_trip(user.id, trip):
        raise ValueError("Traveler has overlapping trip")

    traveler = Traveler(user_id=user.id, trip_id=trip.id)

    db.session.add(traveler)
    db.session.commit()

    return traveler


def remove_traveler(trip_id, id):
    traveler = Traveler.query.filter_by(
        id=id,
        trip_id=trip_id
    ).first()

    if not traveler:
        raise ValueError("Traveler Not Found")

    db.session.delete(traveler)
    db.session.commit()


def has_overlapping_trip(user_id, new_trip):
    existing_memberships = Traveler.query.filter_by(user_id=user_id).all()

    for membership in existing_memberships:
        existing_trip = membership.trip

        if (existing_trip.start_date <= new_trip.end_date and
           new_trip.start_date <= existing_trip.end_date):
            return True

    return False
