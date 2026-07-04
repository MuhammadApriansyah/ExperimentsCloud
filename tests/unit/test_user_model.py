from datetime import datetime

from app.extensions import db
from app.models.user import User


def test_create_user(app):

    with app.app_context():

        user = User(
            username="michi",
            email="michi@example.com",
        )

        user.set_password("secret123")

        db.session.add(user)
        db.session.commit()

        assert user.id is not None


def test_username(app):

    with app.app_context():

        user = User(
            username="michi",
            email="michi@example.com",
        )

        assert user.username == "michi"


def test_email(app):

    with app.app_context():

        user = User(
            username="michi",
            email="michi@example.com",
        )

        assert user.email == "michi@example.com"


def test_password_is_hashed(app):

    with app.app_context():

        user = User()

        user.set_password("secret123")

        assert user.password_hash != "secret123"


def test_check_password(app):

    with app.app_context():

        user = User()

        user.set_password("secret123")

        assert user.check_password("secret123")
        assert not user.check_password("wrongpassword")


def test_created_at_default(app):

    with app.app_context():

        user = User(
            username="michi",
            email="michi@example.com",
        )

        user.set_password("secret123")

        db.session.add(user)
        db.session.commit()

        assert isinstance(user.created_at, datetime)


def test_repr(app):

    with app.app_context():

        user = User(
            username="michi",
            email="michi@example.com",
        )

        assert repr(user) == "<User michi>"
