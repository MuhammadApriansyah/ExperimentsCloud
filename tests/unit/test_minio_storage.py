import pytest

from app.storage.minio import MinIOStorage


def test_minio_storage_is_backend():

    storage = MinIOStorage()

    assert isinstance(
        storage,
        MinIOStorage,
    )


def test_object_key_not_implemented():

    storage = MinIOStorage()

    with pytest.raises(NotImplementedError):

        storage.object_key(
            1,
            "hello.txt",
        )

def test_save_not_implemented():

    storage = MinIOStorage()

    with pytest.raises(NotImplementedError):

        storage.save(
            None,
            "hello.txt",
        )


def test_exists_not_implemented():

    storage = MinIOStorage()

    with pytest.raises(NotImplementedError):

        storage.exists(
            "hello.txt",
        )


def test_delete_not_implemented():

    storage = MinIOStorage()

    with pytest.raises(NotImplementedError):

        storage.delete(
            "hello.txt",
        )


def test_open_not_implemented():

    storage = MinIOStorage()

    with pytest.raises(NotImplementedError):

        storage.open(
            "hello.txt",
        )
