import pytest

from app.storage.local import LocalStorage
from app.storage.manager import get_storage


def test_get_storage_returns_local_storage(app):

    with app.app_context():

        storage = get_storage()

        assert isinstance(
            storage,
            LocalStorage,
        )


def test_get_storage_uses_configured_root(app):

    with app.app_context():

        storage = get_storage()

        assert (
            storage.root
            == app.config["USER_STORAGE"]
        )


def test_unknown_backend_raises_runtime_error(app):

    with app.app_context():

        app.config["STORAGE_BACKEND"] = "unknown"

        with pytest.raises(RuntimeError):

            get_storage()


def test_unknown_backend_message(app):

    with app.app_context():

        app.config["STORAGE_BACKEND"] = "unknown"

        with pytest.raises(RuntimeError) as exc:

            get_storage()

        assert (
            "Unknown storage backend"
            in str(exc.value)
        )


def test_get_storage_returns_s3(app):

    with app.app_context():

        app.config["STORAGE_BACKEND"] = "s3"

        storage = get_storage()

        from app.storage.s3 import S3Storage

        assert isinstance(
            storage,
            S3Storage,
        )


def test_get_storage_returns_minio(app):

    with app.app_context():

        app.config["STORAGE_BACKEND"] = "minio"

        storage = get_storage()

        from app.storage.minio import MinIOStorage

        assert isinstance(
            storage,
            MinIOStorage,
        )
