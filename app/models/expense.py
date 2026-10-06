from app.extensions import db


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