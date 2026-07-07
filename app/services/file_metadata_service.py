from app.extensions import db
from app.models.file_metadata import FileMetadata

from app.storage.manager import get_storage
from app.services.metadata_generator import MetadataGenerator
from app.services.video_metadata_service import VideoMetadataService


class FileMetadataService:

    @staticmethod
    def create(file):

        storage = get_storage()

        path = storage.object_key(
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

        if file.mime_type.startswith("video/"):

            video = VideoMetadataService.extract(path)

            metadata.duration = video.get("duration")
            metadata.image_width = video.get("width")
            metadata.image_height = video.get("height")

        db.session.add(metadata)

        return metadata
