from app.helpers.file_helper import (
    format_file_size,
)


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
