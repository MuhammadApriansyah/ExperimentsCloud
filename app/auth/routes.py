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
    current_user,
)

from app.auth.forms import (
    RegisterForm,
    LoginForm,
)

from app.extensions import db
from app.models import User

from app.constants.messages import (
    FLASH_REGISTER_SUCCESS,
    FLASH_LOGIN_SUCCESS,
    FLASH_LOGOUT_SUCCESS,
    FLASH_USERNAME_EXISTS,
    FLASH_EMAIL_EXISTS,
    FLASH_INVALID_LOGIN,
)

from app.services.logging_service import logger


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
            flash(
                FLASH_USERNAME_EXISTS,
                "danger",
            )
            return redirect(url_for("auth.register"))

        if User.query.filter_by(email=form.email.data).first():
            flash(
                FLASH_EMAIL_EXISTS,
                "danger",
            )
            return redirect(url_for("auth.register"))

        user = User(
            username=form.username.data,
            email=form.email.data,
        )

        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash(
            FLASH_REGISTER_SUCCESS,
            "success",
        )

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

            logger.info(
                "LOGIN | user=%s",
                user.email,
            )

            flash(
                FLASH_LOGIN_SUCCESS,
                "success",
            )

            return redirect(
                url_for("auth.dashboard")
            )

        flash(
            FLASH_INVALID_LOGIN,
            "danger",
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

    logger.info(
        "LOGOUT | user=%s",
        current_user.email,
    )

    logout_user()

    flash(
        FLASH_LOGOUT_SUCCESS,
        "danger",
    )

    return redirect(
        url_for("auth.login")
    )
