#!/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flasggster import Swagger
from api.routes.tv import bp as tv_bp
from api.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.logger.setLevel("INFO")

    db.init_app(app)

    Swagger(app)

    socketio.init_app(app)

    from api.routes.health import bp as health_bp
    from api.routes.auth import bp as auto_bp
    from api.routes.trending import bp as trending_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(auto_bp)
    app.register_blueprint(trending_bp)

    @socketio.on("ping")
    def ping():
        return {"message": "pong"}

    return app

# local run
if __name__ == "__main__":
    app = create_app()
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
