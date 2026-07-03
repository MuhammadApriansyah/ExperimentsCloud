from pathlib import Path

from flask_login import current_user

from app.extensions import db

from app.models import File

from app.files.utils import (
    generate_stored_name,
    user_directory,
)

from app.files.validators import (
    FileValidator,
)

from app.services.storage_service import (
    StorageService,
)


class FileService:

    @staticmethod
    def upload(uploaded_file):

        FileValidator.validate_extension(
            uploaded_file.filename
        )

        uploaded_file.seek(0, 2)
        size = uploaded_file.tell()
        uploaded_file.seek(0)

        FileValidator.validate_size(size)

        extension = (
            Path(uploaded_file.filename)
            .suffix
            .lstrip(".")
        )

        stored_name = generate_stored_name(
            extension
        )

        directory = user_directory(
            current_user.id
        )

        destination = (
            directory /
            stored_name
        )

        StorageService.save(
            uploaded_file,
            destination,
        )

        file = File(
            owner=current_user,
            original_name=uploaded_file.filename,
            stored_name=stored_name,
            file_extension=extension,
            mime_type=uploaded_file.mimetype,
            file_size=size,
            storage_path=str(destination),
        )

        db.session.add(file)
        db.session.commit()

        return file

    @staticmethod
    def list_files(user):

        return (
            File.query
            .filter_by(owner_id=user.id)
            .order_by(File.created_at.desc())
            .all()
        )

