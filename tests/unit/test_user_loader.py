import pytest

from app.auth.user_loader import load_user
from app.extensions import db
from app.models.user import User


def create_user():

    user = User(
        username="michi",
        email="michi@example.com",
    )

    user.set_password("secret123")

    db.session.add(user)
    db.session.commit()

    return user


def test_load_existing_user(app):

    with app.app_context():

        user = create_user()

        loaded = load_user(str(user.id))

        assert loaded == user


def test_load_missing_user(app):

    with app.app_context():

        assert load_user("9999") is None


def test_load_user_accepts_string_id(app):

    with app.app_context():

        user = create_user()

        loaded = load_user(str(user.id))

        assert loaded.id == user.id


def test_load_user_invalid_id(app):

    with app.app_context():

        with pytest.raises(ValueError):

            load_user("abc")
