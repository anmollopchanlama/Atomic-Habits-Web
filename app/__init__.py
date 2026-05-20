from flask import Flask
from app.routes import authRoutes
from app.database import get_connection
import config

def create_app():
    app = Flask(__name__)
    app.secret_key = config.SECRET_KEY
    get_connection()
    app.register_blueprint(authRoutes.register())
    return app