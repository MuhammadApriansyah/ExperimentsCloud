from .backend import StorageBackend


class MinIOStorage(StorageBackend):

    def __init__(self, root=None):
        self.root = root

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
