from pathlib import Path
from unittest.mock import Mock

from app.services.storage_service import StorageService

from app.storage.key_builder import StorageKeyBuilder


def test_user_directory(app):

    with app.app_context():

        path = StorageService.user_directory(
            10
        )

        assert path == app.config["USER_STORAGE"] / "10"


def test_file_path(app):

    with app.app_context():

        path = StorageService.file_path(
            5,
            "example.txt",
        )

        assert path == (
            app.config["USER_STORAGE"]
            / "5"
            / "example.txt"
        )


def test_ensure_directory(tmp_path):

    directory = tmp_path / "storage"

    StorageService.ensure_directory(directory)

    assert directory.exists()
    assert directory.is_dir()


def test_exists(tmp_path):

    file = tmp_path / "sample.txt"

    file.write_text("hello")

    assert StorageService.exists(file)


def test_delete(tmp_path):

    file = tmp_path / "delete.txt"

    file.write_text("hello")

    StorageService.delete(file)

    assert not file.exists()


def test_save(tmp_path):

    destination = tmp_path / "upload" / "example.txt"

    uploaded_file = Mock()

    StorageService.save(
        uploaded_file,
        destination,
    )

    uploaded_file.save.assert_called_once_with(
        destination
    )

    assert destination.parent.exists()
