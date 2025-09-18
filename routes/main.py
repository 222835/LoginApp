from flask import Blueprint, render_template, session, redirect, url_for, flash

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    if session.get("user_id"):
        return redirect(url_for("main.home"))
    return redirect(url_for("auth.login"))

@main_bp.route("/home")
def home():
    if not session.get("user_id"):
        flash("Debes iniciar sesión.", "warning")
        return redirect(url_for("auth.login"))
    return render_template("home.html", username=session.get("username"))
