import os
from flask import Flask, session, request, abort
from app.routes import authRoutes
from app.database import get_connection
import config

def create_app():
    app = Flask(__name__)
    app.secret_key = config.SECRET_KEY
    get_connection()
    app.register_blueprint(authRoutes.register())

    @app.before_request
    def csrf_protect():
        # 1. ONLY generate a brand new token on page view GET requests
        if request.method == "GET":
            if "csrf_token" not in session:
                session["csrf_token"] = os.urandom(16).hex()

        # 2. Handle security verification on POST requests
        if request.method == "POST":
            token = request.form.get("csrf_token") or request.files.get("csrf_token")
            
            # Use session.get() safely so we don't accidentally generate a new one
            expected_token = session.get("csrf_token")
            
            if not token or token != expected_token:
                abort(403)

    return app
