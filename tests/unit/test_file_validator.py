import pytest

from app.files.validators import FileValidator
from app.exceptions.file import (
    InvalidFileExtension,
    FileTooLarge,
)


def test_validate_extension_accepts_txt(app):

    with app.app_context():

        FileValidator.validate_extension("document.txt")


def test_validate_extension_rejects_exe(app):

    with app.app_context():

        with pytest.raises(InvalidFileExtension):

            FileValidator.validate_extension("virus.exe")


def test_validate_size_accepts_small_file(app):

    with app.app_context():

        FileValidator.validate_size(1024)


def test_validate_size_rejects_large_file(app):

    with app.app_context():

        with pytest.raises(FileTooLarge):

            FileValidator.validate_size(
                app.config["MAX_UPLOAD_SIZE"] + 1
            )
