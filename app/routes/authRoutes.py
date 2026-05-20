from flask import Blueprint
from app.controllers import authController

bp = Blueprint("auth", __name__)

def register():
    bp.route("/login", methods=["GET", "POST"])(authController.login)
    bp.route("/")(authController.home)
    bp.route("/about")(authController.about)
    bp.route("/register", methods=["GET", "POST"])(authController.register)
    return bp