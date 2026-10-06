from app.extensions import db


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