from pathlib import Path

from app.extensions import db
from app.models import File, FileMetadata, User
from app.services.file_metadata_service import FileMetadataService
from app.services.storage_service import StorageService
from pypdf import PdfWriter

from unittest.mock import patch

import subprocess


def create_user():

    user = User(
        username="michi",
        email="michi@example.com",
    )

    user.set_password("secret123")

    db.session.add(user)
    db.session.commit()

    return user


def create_file(app, user):

    stored_name = "example.txt"

    path = StorageService.object_key(
        user.id,
        stored_name,
    )

    StorageService.ensure_directory(
        path.parent,
    )

    path.write_text("ExperimentsCloud")

    file = File(
        owner=user,
        original_name="example.txt",
        stored_name=stored_name,
        file_extension="txt",
        mime_type="text/plain",
        file_size=path.stat().st_size,
    )

    db.session.add(file)
    db.session.commit()

    return file

def create_video_file(app, user):

    stored_name = "video.mp4"

    path = StorageService.object_key(
        user.id,
        stored_name,
    )

    StorageService.ensure_directory(
        path.parent,
    )

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "lavfi",
            "-i",
            "color=c=black:s=320x240:d=1",
            "-c:v",
            "libx264",
            str(path),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    file = File(
        owner=user,
        original_name="video.mp4",
        stored_name=stored_name,
        file_extension="mp4",
        mime_type="video/mp4",
        file_size=path.stat().st_size,
    )

    db.session.add(file)
    db.session.commit()

    return file


def test_create_metadata(app):

    with app.app_context():

        user = create_user()

        file = create_file(app, user)

        metadata = FileMetadataService.create(file)

        db.session.commit()

        assert metadata.file_id == file.id

        assert metadata.checksum is not None

        assert len(metadata.checksum) == 64

        assert metadata.page_count is None


def test_relationship(app):

    with app.app_context():

        user = create_user()

        file = create_file(app, user)

        FileMetadataService.create(file)

        db.session.commit()

        refreshed = db.session.get(
            File,
            file.id,
        )

        assert refreshed.file_metadata is not None

        assert (
            refreshed.file_metadata.file_id
            == refreshed.id
        )


def test_metadata_saved(app):

    with app.app_context():

        user = create_user()

        file = create_file(app, user)

        FileMetadataService.create(file)

        db.session.commit()

        assert (
            FileMetadata.query.count()
            == 1
        )


def test_create_pdf_metadata(app):

    with app.app_context():

        user = create_user()

        file = create_pdf_file(
            app,
            user,
            pages=3,
        )

        metadata = FileMetadataService.create(file)

        db.session.commit()

        assert metadata.page_count == 3

        assert metadata.checksum is not None

        assert metadata.file_id == file.id


def create_pdf_file(app, user, pages=3):

    stored_name = "example.pdf"

    path = StorageService.object_key(
        user.id,
        stored_name,
    )

    StorageService.ensure_directory(
        path.parent,
    )

    writer = PdfWriter()

    for _ in range(pages):
        writer.add_blank_page(
            width=595,
            height=842,
        )

    with path.open("wb") as pdf_file:
        writer.write(pdf_file)

    file = File(
        owner=user,
        original_name="example.pdf",
        stored_name=stored_name,
        file_extension="pdf",
        mime_type="application/pdf",
        file_size=path.stat().st_size,
    )

    db.session.add(file)
    db.session.commit()

    return file


def create_audio_file(app, user):

    stored_name = "example.mp3"

    path = StorageService.object_key(
        user.id,
        stored_name,
    )

    StorageService.ensure_directory(
        path.parent,
    )

    path.write_bytes(b"dummy audio")

    file = File(
        owner=user,
        original_name="example.mp3",
        stored_name=stored_name,
        file_extension="mp3",
        mime_type="audio/mpeg",
        file_size=path.stat().st_size,
    )

    db.session.add(file)
    db.session.commit()

    return file


@patch(
    "app.services.file_metadata_service.MetadataGenerator.audio_duration"
)
def test_create_audio_metadata(
    audio_duration_mock,
    app,
):

    audio_duration_mock.return_value = 215

    with app.app_context():

        user = create_user()

        file = create_audio_file(
            app,
            user,
        )

        metadata = FileMetadataService.create(file)

        db.session.commit()

        assert metadata.duration == 215

        assert metadata.page_count is None

        assert metadata.image_width is None

        assert metadata.image_height is None

        assert metadata.checksum is not None

        audio_duration_mock.assert_called_once()


def test_create_video_metadata(app):

    with app.app_context():

        user = create_user()

        file = create_video_file(
            app,
            user,
        )

        metadata = FileMetadataService.create(
            file,
        )

        db.session.commit()

        assert metadata.file_id == file.id

        assert metadata.checksum is not None

        assert metadata.duration is not None

        assert metadata.image_width == 320

        assert metadata.image_height == 240
