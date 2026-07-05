from app.extensions import db
from app.models.file_metadata import FileMetadata

from app.services.storage_service import StorageService
from app.services.metadata_generator import MetadataGenerator


class FileMetadataService:

    @staticmethod
    def create(file):

        path = StorageService.file_path(
            file.owner_id,
            file.stored_name,
        )

        metadata = FileMetadata(
            file=file,
            checksum=MetadataGenerator.checksum(path),
        )

        if file.mime_type.startswith("image/"):

            width, height = MetadataGenerator.image_size(path)

            metadata.image_width = width
            metadata.image_height = height

        if file.mime_type == "application/pdf":

            metadata.page_count = (
               MetadataGenerator.pdf_page_count(
                   path
               )
            )

        if file.mime_type.startswith("audio/"):

            metadata.duration = (
                MetadataGenerator.audio_duration(
                    path
                )
            )

        db.session.add(metadata)

        return metadata
