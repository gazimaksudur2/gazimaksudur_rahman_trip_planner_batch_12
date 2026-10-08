from flask import Flask, jsonify
from app.extensions import db
from app.exceptions import BusinessException, NotFoundException


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = ("sqlite:///trip_planner.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    @app.errorhandler(BusinessException)
    def handle_business_exception(error):
        return jsonify({"error": error.message}), 400

    @app.errorhandler(NotFoundException)
    def handle_not_found_exception(error):
        return jsonify({"error": error.message}), 404

    from app.routes import register_routes
    register_routes(app)

    with app.app_context():
        from app import models
        db.create_all()

    return app
