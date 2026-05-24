from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from models.user_model import User

from models.extensions import db
from models.extensions import bcrypt


auth = Blueprint("auth", __name__)


# REGISTER

@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")

        email = request.form.get("email")

        password = request.form.get("password")

        # CHECK EXISTING USER

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:

            flash(
                "Email Already Exists",
                "danger"
            )

            return redirect(
                url_for("auth.register")
            )

        # PASSWORD HASHING

        hashed_password = bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

        # CREATE USER

        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)

        db.session.commit()

        flash(
            "Registration Successful! Please Login",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template("register.html")


# LOGIN

@auth.route("/", methods=["GET", "POST"])

@auth.route("/login", methods=["GET", "POST"])

def login():

    if request.method == "POST":

        email = request.form.get("email")

        password = request.form.get("password")

        # CHECK USER

        user = User.query.filter_by(
            email=email
        ).first()

        # USER NOT REGISTERED

        if not user:

            flash(
                "Register Required",
                "danger"
            )

            return redirect(
                url_for("auth.register")
            )

        # WRONG PASSWORD

        if not bcrypt.check_password_hash(
            user.password,
            password
        ):

            flash(
                "Incorrect Password",
                "danger"
            )

            return redirect(
                url_for("auth.login")
            )

        # LOGIN SUCCESS

        login_user(user)

        flash(
            "Login Successful",
            "success"
        )

        return redirect("/dashboard")

    return render_template("login.html")


# LOGOUT

@auth.route("/logout")

@login_required

def logout():

    logout_user()

    flash(
        "Logged Out Successfully",
        "info"
    )

    return redirect(
        url_for("auth.login")
    )