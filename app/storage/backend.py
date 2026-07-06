from abc import ABC, abstractmethod


class StorageBackend(ABC):

    @abstractmethod
    def file_path(
        self,
        user_id: int,
        stored_name: str,
    ):
        pass

    @abstractmethod
    def save(
        self,
        uploaded_file,
        destination,
    ):
        pass

    @abstractmethod
    def exists(
        self,
        path,
    ):
        pass

    @abstractmethod
    def delete(
        self,
        path,
    ):
        pass

    @abstractmethod
    def open(
        self,
        path,
    ):
        pass
