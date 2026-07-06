from app.storage.key_builder import StorageKeyBuilder

from .backend import StorageBackend


class MinIOStorage(StorageBackend):

    def __init__(self, root=None):
        self.root = root

    def key(
        self,
        user_id: int,
        stored_name: str,
    ):
        return StorageKeyBuilder.user_file(
            user_id,
            stored_name,
        )

    def resolve(self, key):
        return key

    def file_path(
        self,
        user_id: int,
        stored_name: str,
    ):
        raise NotImplementedError

    def save(
        self,
        uploaded_file,
        destination,
    ):
        raise NotImplementedError

    def exists(
        self,
        path,
    ):
        raise NotImplementedError

    def delete(
        self,
        path,
    ):
        raise NotImplementedError

    def open(
        self,
        path,
    ):
        raise NotImplementedError
