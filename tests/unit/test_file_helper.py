from app.helpers.file_helper import (
    format_file_size,
)

from app.helpers import get_file_icon

from app.helpers import get_file_type


def test_format_bytes():

    assert format_file_size(512) == "512 B"


def test_format_kilobytes():

    assert format_file_size(2048) == "2 KB"


def test_format_megabytes():

    assert (
        format_file_size(3145728)
        == "3 MB"
    )


def test_format_zero():

    assert format_file_size(0) == "0 B"


def test_pdf_icon():

    assert get_file_icon("pdf") == "📄"


def test_image_icon():

    assert get_file_icon("jpg") == "🖼"


def test_text_icon():

    assert get_file_icon("txt") == "📝"


def test_unknown_icon():

    assert get_file_icon("xyz") == "📁"


def test_pdf_type():

    assert (
        get_file_type("pdf")
        == "PDF Document"
    )


def test_txt_type():

    assert (
        get_file_type("txt")
        == "Text File"
    )


def test_png_type():

    assert (
        get_file_type("png")
        == "PNG Image"
    )


def test_zip_type():

    assert (
        get_file_type("zip")
        == "ZIP Archive"
    )


def test_unknown_type():

    assert (
        get_file_type("xyz")
        == "Unknown File"
    )
