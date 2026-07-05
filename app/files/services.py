from pathlib import Path

from app.extensions import db

from app.models import File

from app.files.utils import generate_stored_name

from app.files.validators import (
    FileValidator,
)

from app.services.storage_service import (
    StorageService,
)
from app.services.logging_service import logger

from app.services.file_metadata_service import (
    FileMetadataService,
)


class FileService:

    @staticmethod
    def upload(
        uploaded_file,
        user,
        folder=None,
    ):

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
            .lower()
            .lstrip(".")
        )

        stored_name = generate_stored_name(
            extension
        )

        destination = StorageService.file_path(
            user.id,
            stored_name,
        )

        StorageService.save(
            uploaded_file,
            destination,
        )

        file = File(
            owner=user,
            folder=folder,
            original_name=uploaded_file.filename,
            stored_name=stored_name,
            file_extension=extension,
            mime_type=uploaded_file.mimetype,
            file_size=size,
        )

        db.session.add(file)
        db.session.flush()
        FileMetadataService.create(file)
        db.session.commit()

        return file

    @staticmethod
    def list_files(
        user,
        folder=None,
    ):

        query = File.query.filter_by(
            owner_id=user.id,
        )

        if folder is None:

            query = query.filter_by(
                folder_id=None,
            )

        else:

            query = query.filter_by(
                folder_id=folder.id,
            )

        return (
            query
            .order_by(
                File.created_at.desc()
            )
            .all()
        )

    @staticmethod
    def get_user_file(file_id, user_id):
        return File.query.filter_by(
            id=file_id,
            owner_id=user_id
        ).first()

    @staticmethod
    def delete(file):

        path = StorageService.file_path(
            file.owner_id,
            file.stored_name,
        )

        StorageService.delete(path)

        db.session.delete(file)

        db.session.commit()

    @staticmethod
    def rename(file, new_name):

        old_name = file.original_name

        extension = Path(old_name).suffix

        new_name = Path(new_name).stem.strip()

        file.original_name = f"{new_name}{extension}"

        db.session.commit()

        logger.info(
            "RENAME | user=%s | %s -> %s",
            file.owner_id,
            old_name,
            file.original_name,
        )

        return file
