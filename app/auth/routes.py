from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
)

from app.auth.forms import (
    RegisterForm,
    LoginForm,
)

from app.extensions import db
from app.models import User


auth = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@auth.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        if User.query.filter_by(username=form.username.data).first():
            flash("Username sudah digunakan.", "danger")
            return redirect(url_for("auth.register"))

        if User.query.filter_by(email=form.email.data).first():
            flash("Email sudah terdaftar.", "danger")
            return redirect(url_for("auth.register"))

        user = User(
            username=form.username.data,
            email=form.email.data,
        )

        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("Registrasi berhasil. Silakan login.", "success")

        return redirect(url_for("auth.login"))

    return render_template(
        "auth/register.html",
        form=form
    )

@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and user.check_password(
            form.password.data
        ):

            login_user(user)

            flash(
                "Login berhasil.",
                "success"
            )

            return redirect(
                url_for("auth.dashboard")
            )

        flash(
            "Email atau password salah.",
            "danger"
        )

    return render_template(
        "auth/login.html",
        form=form
    )

@auth.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "auth/dashboard.html"
    )

@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "Anda telah logout.",
        "success"
    )

    return redirect(
        url_for("auth.login")
    )
