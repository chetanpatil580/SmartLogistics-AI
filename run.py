import os
import sys
from flask import Flask
from config import Config

def create_app():
    # Set templates and static paths in views/
    templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "views", "templates")
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "views", "static")

    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
    app.config.from_object(Config)

    # Register Controller Blueprints (MVC)
    from controllers.dashboard_controller import dashboard_bp
    from controllers.order_controller import order_bp
    from controllers.fleet_controller import fleet_bp
    from controllers.shipment_controller import shipment_bp
    from controllers.warehouse_controller import warehouse_bp
    from controllers.route_controller import route_bp
    from controllers.driver_controller import driver_bp
    from controllers.cost_controller import cost_bp
    from controllers.analytics_controller import analytics_bp
    from controllers.alert_controller import alert_bp
    from controllers.ai_controller import ai_bp

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(fleet_bp)
    app.register_blueprint(shipment_bp)
    app.register_blueprint(warehouse_bp)
    app.register_blueprint(route_bp)
    app.register_blueprint(driver_bp)
    app.register_blueprint(cost_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(alert_bp)
    app.register_blueprint(ai_bp)

    return app

if __name__ == "__main__":
    # Ensure database exists
    db_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database", "logistics.db")
    if not os.path.exists(db_file):
        print("Database not found. Initializing database...")
        from database.init_db import init_database
        init_database()

    app = create_app()
    print("*" * 65)
    print("   AI LOGISTICS CONTROL TOWER - MVC SYSTEM READY")
    print(f"   Web Dashboard running on: http://{Config.HOST}:{Config.PORT}")
    print("*" * 65)
    app.run(host=Config.HOST, port=Config.PORT, debug=False)
