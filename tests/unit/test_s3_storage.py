import pytest

from app.storage.s3 import S3Storage


def test_s3_storage_is_backend():

    storage = S3Storage()

    assert isinstance(
        storage,
        S3Storage,
    )


