from flask import Flask

from config import Config
from models.extensions import db
from models.extensions import bcrypt
from models.extensions import login_manager
from models.extensions import socketio

from websocket.socket_events import register_socket_events


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    bcrypt.init_app(app)

    login_manager.init_app(app)

    socketio.init_app(app)

    login_manager.login_view = "auth.login"

    register_socket_events(socketio)

    from routes.auth_routes import auth
    from routes.task_routes import task

    app.register_blueprint(auth)

    app.register_blueprint(task)

    # AUTO CREATE DATABASE TABLES
    with app.app_context():
        db.create_all()

    return app


app = create_app()
if __name__ == "__main__":

    socketio.run(

        app,

        host="0.0.0.0",

        port=5000,

        debug=True
    )
