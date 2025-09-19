from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models import User
from sqlalchemy.exc import IntegrityError

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        if not username or not password:
            flash("Usuario y contraseña requeridos", "warning")
            return redirect(url_for("auth.register"))

        pw_hash = generate_password_hash(password)

        db_session = db.session()
        new_user = User(username=username, password=pw_hash)
        db_session.add(new_user)

        try:
            db_session.commit()
            flash("Registrado correctamente.", "success")
            return redirect(url_for("auth.login"))
        except IntegrityError:
            db_session.rollback()
            flash("El usuario ya existe.", "danger")
        finally:
            db_session.close()

    return render_template("register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        db_session = db.session()
        user = db_session.query(User).filter_by(username=username).first()
        db_session.close()

        if not user:
            flash("Usuario no encontrado.", "danger")
            return redirect(url_for("auth.login"))

        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            return redirect(url_for("main.home"))
        else:
            flash("Contraseña incorrecta.", "danger")

    return render_template("login.html")

@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("Sesión cerrada.", "info")
    return redirect(url_for("auth.login"))
