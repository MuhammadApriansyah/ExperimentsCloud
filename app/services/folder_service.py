from app.extensions import db

from app.models import Folder

from app.services.logging_service import logger


class FolderService:

    @staticmethod
    def create(name, owner, parent=None):

        name = name.strip()

        if not name:
            raise ValueError("Folder name cannot be empty")

        folder = Folder(
            name=name,
            owner=owner,
            parent=parent,
        )

        db.session.add(folder)

        logger.info(
            "CREATE_FOLDER | user=%s | folder=%s",
            owner.id,
            folder.name,
        )

        db.session.commit()

        return folder

    @staticmethod
    def list_root(owner):

        return (
            Folder.query
            .filter_by(
                owner_id=owner.id,
                parent_id=None,
            )
            .order_by(Folder.name.asc())
            .all()
        )

    @staticmethod
    def get_user_folder(folder_id, user_id):

        return (
            Folder.query
            .filter_by(
                id=folder_id,
                owner_id=user_id,
            )
            .first()
        )

    @staticmethod
    def rename(folder, new_name):

        old_name = folder.name

        new_name = new_name.strip()

        if not new_name:
            raise ValueError("Folder name cannot be empty")

        folder.name = new_name

        logger.info(
            "RENAME_FOLDER | user=%s | %s -> %s",
            folder.owner_id,
            old_name,
            folder.name,
        )

        db.session.commit()

        return folder

    @staticmethod
    def delete(folder):

        db.session.delete(folder)

        logger.info(
            "DELETE_FOLDER | user=%s | folder=%s",
            folder.owner_id,
            folder.name,
        )

        db.session.commit()
