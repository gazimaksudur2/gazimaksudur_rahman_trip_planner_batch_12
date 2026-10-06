from flask import Flask
from app.extensions import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = ("sqlite:///trip_planner.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.routes import register_routes
    register_routes(app)

    with app.app_context():
        from app import models  # noqa: F401
        db.create_all()

    return app