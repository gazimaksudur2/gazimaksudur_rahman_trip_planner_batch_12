from app.routes.health import health_bp
from app.routes.trip_routes import trip_bp
from app.routes.traveler_routes import traveler_bp
from app.routes.expense_routes import expense_bp


def register_routes(app):
    app.register_blueprint(health_bp)
    app.register_blueprint(trip_bp)
    app.register_blueprint(expense_bp)
    app.register_blueprint(traveler_bp)
