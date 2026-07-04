from datetime import datetime

from app.extensions import db
from app.models.file import File
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


def create_file(user):

    file = File(
        owner=user,
        original_name="document.txt",
        stored_name="abc123.txt",
        file_extension="txt",
        mime_type="text/plain",
        file_size=1024,
    )

    db.session.add(file)
    db.session.commit()

    return file


def test_create_file(app):

    with app.app_context():

        user = create_user()

        file = create_file(user)

        assert file.id is not None


def test_original_name(app):

    with app.app_context():

        user = create_user()

        file = create_file(user)

        assert file.original_name == "document.txt"


def test_stored_name(app):

    with app.app_context():

        user = create_user()

        file = create_file(user)

        assert file.stored_name == "abc123.txt"


def test_file_extension(app):

    with app.app_context():

        user = create_user()

        file = create_file(user)

        assert file.file_extension == "txt"


def test_mime_type(app):

    with app.app_context():

        user = create_user()

        file = create_file(user)

        assert file.mime_type == "text/plain"


def test_file_size(app):

    with app.app_context():

        user = create_user()

        file = create_file(user)

        assert file.file_size == 1024


def test_created_at_default(app):

    with app.app_context():

        user = create_user()

        file = create_file(user)

        assert isinstance(file.created_at, datetime)


def test_owner_relationship(app):

    with app.app_context():

        user = create_user()

        file = create_file(user)

        assert file.owner == user


def test_repr(app):

    with app.app_context():

        user = create_user()

        file = create_file(user)

        assert repr(file) == "<File document.txt>"
