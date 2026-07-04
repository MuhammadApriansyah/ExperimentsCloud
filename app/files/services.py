from pathlib import Path

from flask_login import current_user

from app.extensions import db

from app.models import File

from app.files.utils import generate_stored_name

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

        StorageService.file_path(
            current_user.id,
            file.stored_name,
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

    @staticmethod
    def get_user_file(file_id, user_id):
        return File.query.filter_by(
            id=file_id,
            owner_id=user_id
        ).first()
