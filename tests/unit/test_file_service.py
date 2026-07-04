from io import BytesIO
from unittest.mock import Mock, patch

from app.extensions import db
from app.models.file import File
from app.models.user import User
from app.files.services import FileService


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


def test_list_files(app):

    with app.app_context():

        user = create_user()

        create_file(user)

        files = FileService.list_files(user)

        assert len(files) == 1


def test_get_user_file(app):

    with app.app_context():

        user = create_user()

        file = create_file(user)

        result = FileService.get_user_file(
            file.id,
            user.id,
        )

        assert result == file


def test_delete(app):

    with app.app_context():

        user = create_user()

        file = create_file(user)

        FileService.delete(file)

        assert File.query.count() == 0


@patch("app.files.services.StorageService.save")
@patch("app.files.services.StorageService.file_path")
@patch("app.files.services.generate_stored_name")
@patch("app.files.services.FileValidator.validate_size")
@patch("app.files.services.FileValidator.validate_extension")
def test_upload(
    validate_extension_mock,
    validate_size_mock,
    generate_name_mock,
    file_path_mock,
    save_mock,
    app,
):

    with app.app_context():

        user = create_user()

        generate_name_mock.return_value = "stored.txt"

        file_path_mock.return_value = Mock()

        uploaded = Mock()

        uploaded.filename = "document.txt"
        uploaded.mimetype = "text/plain"

        uploaded.seek = Mock()

        uploaded.tell = Mock(return_value=1024)

        file = FileService.upload(
            uploaded,
            user,
        )

        validate_extension_mock.assert_called_once()

        validate_size_mock.assert_called_once_with(1024)

        generate_name_mock.assert_called_once_with("txt")

        save_mock.assert_called_once()

        assert file.original_name == "document.txt"

        assert file.stored_name == "stored.txt"

        assert File.query.count() == 1
