from datetime import datetime
from app import db


class Trip(db.Model):

    __tablename__ = "trips"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    destination = db.Column(
        db.String(200),
        nullable=False
    )

    start_date = db.Column(
        db.Date,
        nullable=False
    )

    end_date = db.Column(
        db.Date,
        nullable=False
    )

    budget = db.Column(
        db.Float,
        nullable=False
    )

    max_travelers = db.Column(
        db.Integer,
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="PLANNED"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    travelers = db.relationship(
        "Traveler",
        backref="trip",
        cascade="all, delete"
    )

    expenses = db.relationship(
        "Expense",
        backref="trip",
        cascade="all, delete"
    )


class Traveler(db.Model):
    __tablename__ = "travelers"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    trip_id = db.Column(
        db.Integer,
        db.ForeignKey("trips.id"),
        nullable=False
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        nullable=False
    )


class Expense(db.Model):
    __tablename__ = "expenses"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    trip_id = db.Column(
        db.Integer,
        db.ForeignKey("trips.id"),
        nullable=False
    )

    title = db.Column(
        db.String(100),
        nullable=False
    )

    amount = db.Column(
        db.Float,
        nullable=False
    )
