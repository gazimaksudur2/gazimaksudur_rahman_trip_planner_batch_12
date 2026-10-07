from app.extensions import db
from datetime import datetime


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
        back_populates="trip",
        cascade="all, delete"
    )

    expenses = db.relationship(
        "Expense",
        backref="trip",
        cascade="all, delete"
    )