import uuid

from app.files.utils import generate_stored_name


def test_generate_stored_name_extension():

    filename = generate_stored_name("txt")

    assert filename.endswith(".txt")


def test_generate_stored_name_strips_dot():

    filename = generate_stored_name(".pdf")

    assert filename.endswith(".pdf")


def test_generate_stored_name_lowercase():

    filename = generate_stored_name("JPG")

    assert filename.endswith(".jpg")


def test_generate_stored_name_uuid():

    filename = generate_stored_name("txt")

    value = filename.removesuffix(".txt")

    uuid.UUID(value)


def test_generate_stored_name_unique():

    first = generate_stored_name("txt")

    second = generate_stored_name("txt")

    assert first != second
