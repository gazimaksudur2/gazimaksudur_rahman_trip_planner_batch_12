from app.routes.health import health_bp
from app.routes.trip_routes import trip_bp
from app.routes.traveler_routes import traveler_bp
from app.routes.expense_routes import expense_bp
from app.routes.summary_routes import summary_bp
from app.routes.status_routes import status_bp


def register_routes(app):
    app.register_blueprint(health_bp)
    app.register_blueprint(trip_bp)
    app.register_blueprint(expense_bp)
    app.register_blueprint(traveler_bp)
    app.register_blueprint(summary_bp)
    app.register_blueprint(status_bp)
