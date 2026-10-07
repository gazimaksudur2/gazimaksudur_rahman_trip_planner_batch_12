from app.extensions import db
from datetime import datetime


class Traveler(db.Model):

    __tablename__ = "travelers"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    trip_id = db.Column(
        db.Integer,
        db.ForeignKey("trips.id"),
        nullable=False
    )

    joined_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user = db.relationship(
        "User",
        back_populates="travelers"
    )

    trip = db.relationship(
        "Trip",
        back_populates="travelers"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "user_id",
            "trip_id",
            name="unique_user_trip"
        ),
    )
