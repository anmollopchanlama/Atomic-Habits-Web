from flask import Blueprint
from app.controllers import authController

bp = Blueprint("auth", __name__)

def register():
    bp.route("/login", methods=["GET", "POST"])(authController.login)
    bp.route("/")(authController.home)
    bp.route("/about")(authController.about)
    bp.route("/register", methods=["GET", "POST"])(authController.register)
    bp.route("/admin/dashboard")(authController.admin_dashboard)
    bp.route("/user/dashboard")(authController.user_dashboard)
    return bp