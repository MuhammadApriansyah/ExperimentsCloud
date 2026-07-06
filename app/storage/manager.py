from flask import current_app

from app.storage.local import LocalStorage
from app.storage.s3 import S3Storage
from app.storage.minio import MinIOStorage

_STORAGE_BACKENDS = {
    "local": LocalStorage,
    "s3": S3Storage,
    "minio": MinIOStorage,
}


def get_storage():

    backend_name = current_app.config.get(
        "STORAGE_BACKEND",
        "local",
    )

    backend = _STORAGE_BACKENDS.get(
        backend_name
    )

    if backend is None:
        raise RuntimeError(
            f"Unknown storage backend: {backend_name}"
        )

    if backend_name == "local":
        return backend(
            current_app.config["USER_STORAGE"]
        )

    return backend()


def register_backend(
    name,
    backend,
):

    _STORAGE_BACKENDS[name] = backend


def available_backends():

    return tuple(
        _STORAGE_BACKENDS.keys()
    )
