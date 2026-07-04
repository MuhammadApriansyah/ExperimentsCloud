from io import BytesIO

from app.extensions import db
from app.models.user import User
from app.models.file import File

from flask import current_app


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
        follow_redirects=True,
    )


def upload_file(
    client,
    filename="example.txt",
    content=b"Hello ExperimentsCloud",
):

    return client.post(
        "/files/upload",
        data={
            "file": (
                BytesIO(content),
                filename,
            ),
        },
        content_type="multipart/form-data",
        follow_redirects=False,
    )


def test_files_page_requires_login(client):

    response = client.get(
        "/files/",
        follow_redirects=False,
    )

    assert response.status_code == 302


def test_upload_page_requires_login(client):

    response = client.get(
        "/files/upload",
        follow_redirects=False,
    )

    assert response.status_code == 302


def test_upload_success(client):

    create_user()

    login(client)

    response = upload_file(client)

    assert response.status_code == 302

    assert File.query.count() == 1


def test_upload_invalid_extension(client):

    create_user()

    login(client)

    response = client.post(
        "/files/upload",
        data={
            "file": (
                BytesIO(b"virus"),
                "virus.exe",
            ),
        },
        content_type="multipart/form-data",
        follow_redirects=False,
    )

    assert response.status_code in (400, 500, 302)

    assert File.query.count() == 0


def test_upload_file_too_large(client, app):

    create_user()

    login(client)

    with app.app_context():

        size = current_app.config["MAX_UPLOAD_SIZE"] + 1

    response = client.post(
        "/files/upload",
        data={
            "file": (
                BytesIO(b"a" * size),
                "large.txt",
            ),
        },
        content_type="multipart/form-data",
        follow_redirects=False,
    )

    assert response.status_code in (400, 413, 500, 302)

    assert File.query.count() == 0


def test_download_success(client):

    create_user()

    login(client)

    upload_file(client)

    file = File.query.first()

    response = client.get(
        f"/files/download/{file.id}",
        follow_redirects=False,
    )

    assert response.status_code == 200


def test_delete_success(client):

    create_user()

    login(client)

    upload_file(client)

    file = File.query.first()

    response = client.post(
        f"/files/delete/{file.id}",
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert File.query.count() == 0
