from app.routes.health import health_bp
from app.routes.trip_routes import trip_bp


def register_routes(app):
    app.register_blueprint(health_bp)
    app.register_blueprint(trip_bp)