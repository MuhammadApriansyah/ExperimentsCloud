from pathlib import Path

from app.services.metadata_generator import MetadataGenerator

from PIL import Image

from pypdf import PdfWriter

from types import SimpleNamespace
from unittest.mock import patch


def test_checksum_returns_sha256(tmp_path):

    file = tmp_path / "example.txt"

    file.write_text("ExperimentsCloud")

    checksum = MetadataGenerator.checksum(file)

    assert len(checksum) == 64

    assert isinstance(checksum, str)


def test_checksum_same_file_same_hash(tmp_path):

    file = tmp_path / "example.txt"

    file.write_text("Hello World")

    first = MetadataGenerator.checksum(file)

    second = MetadataGenerator.checksum(file)

    assert first == second


def test_checksum_different_files(tmp_path):

    file1 = tmp_path / "a.txt"

    file2 = tmp_path / "b.txt"

    file1.write_text("AAA")

    file2.write_text("BBB")

    assert (
        MetadataGenerator.checksum(file1)
        !=
        MetadataGenerator.checksum(file2)
    )


def test_checksum_empty_file(tmp_path):

    file = tmp_path / "empty.txt"

    file.touch()

    checksum = MetadataGenerator.checksum(file)

    assert len(checksum) == 64


def test_image_size(tmp_path):

    image = tmp_path / "sample.png"

    Image.new(
        "RGB",
        (320, 240),
    ).save(image)

    width, height = MetadataGenerator.image_size(image)

    assert width == 320
    assert height == 240


def test_square_image(tmp_path):

    image = tmp_path / "square.png"

    Image.new(
        "RGB",
        (512, 512),
    ).save(image)

    width, height = MetadataGenerator.image_size(image)

    assert width == 512
    assert height == 512


def test_pdf_page_count_single_page(tmp_path):

    pdf = tmp_path / "one_page.pdf"

    writer = PdfWriter()
    writer.add_blank_page(width=595, height=842)

    with pdf.open("wb") as file:
        writer.write(file)

    assert MetadataGenerator.pdf_page_count(pdf) == 1


def test_pdf_page_count_multiple_pages(tmp_path):

    pdf = tmp_path / "three_pages.pdf"

    writer = PdfWriter()

    for _ in range(3):
        writer.add_blank_page(width=595, height=842)

    with pdf.open("wb") as file:
        writer.write(file)

    assert MetadataGenerator.pdf_page_count(pdf) == 3


@patch("app.services.metadata_generator.MutagenFile")
def test_audio_duration(mock_mutagen, tmp_path):

    audio = SimpleNamespace(
        info=SimpleNamespace(
            length=183.9,
        )
    )

    mock_mutagen.return_value = audio

    dummy = tmp_path / "sample.mp3"

    dummy.write_bytes(b"dummy")

    assert (
        MetadataGenerator.audio_duration(dummy)
        == 183
    )


@patch("app.services.metadata_generator.MutagenFile")
def test_audio_duration_invalid_file(
    mock_mutagen,
    tmp_path,
):

    mock_mutagen.return_value = None

    dummy = tmp_path / "invalid.mp3"

    dummy.write_bytes(b"")

    assert (
        MetadataGenerator.audio_duration(dummy)
        is None
    )
