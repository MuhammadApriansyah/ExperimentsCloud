from app.models.user import User
from app.extensions import db


def create_user(
    username="michi",
    email="michi@example.com",
    password="secret123",

):

    user = User(
        username=username,
        email=email,
    )

    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return user


def login(client):

    return client.post(
        "/auth/login",
        data={
            "email": "michi@example.com",
            "password": "secret123",
        },
        follow_redirects=False,
    )


def test_register_success(client):

    response = client.post(
        "/auth/register",
        data={
            "username": "alice",
            "email": "alice@example.com",
            "password": "secret123",
            "confirm_password": "secret123",
        },
        follow_redirects=False,
    )

    assert response.status_code == 302

    assert User.query.filter_by(
        email="alice@example.com"
    ).first() is not None


def test_register_duplicate_username(client):

    create_user()

    response = client.post(
        "/auth/register",
        data={
            "username": "michi",
            "email": "another@example.com",
            "password": "secret123",
            "confirm_password": "secret123",
        },
        follow_redirects=False,
    )

    assert response.status_code == 302


def test_register_duplicate_email(client):

    create_user()

    response = client.post(
        "/auth/register",
        data={
            "username": "another",
            "email": "michi@example.com",
            "password": "secret123",
            "confirm_password": "secret123",
        },
        follow_redirects=False,
    )

    assert response.status_code == 302


def test_register_page(client):

    response = client.get("/auth/register")

    assert response.status_code == 200


def test_login_page(client):

    response = client.get("/auth/login")

    assert response.status_code == 200


def test_dashboard_requires_login(client):

    response = client.get(
        "/auth/dashboard",
        follow_redirects=False,
    )

    assert response.status_code == 302


def test_logout_requires_login(client):

    response = client.get(
        "/auth/logout",
        follow_redirects=False,
    )

    assert response.status_code == 302


def test_login_success(client):

    create_user()

    response = client.post(
        "/auth/login",
        data={
            "email": "michi@example.com",
            "password": "secret123",
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert "/auth/dashboard" in response.location


def test_login_invalid_password(client):

    create_user()

    response = client.post(
        "/auth/login",
        data={
            "email": "michi@example.com",
            "password": "wrongpassword",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200


def test_login_unknown_email(client):

    response = client.post(
        "/auth/login",
        data={
            "email": "unknown@example.com",
            "password": "secret123",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200


def test_logout_success(client):

    create_user()

    login(client)

    response = client.get(
        "/auth/logout",
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert "/auth/login" in response.location
