from abc import ABC, abstractmethod


class StorageBackend(ABC):

    @abstractmethod
    def object_key(
        self,
        user_id: int,
        stored_name: str,
    ):
        """
        Return backend-specific object identifier.

        LocalStorage:
            users/1/file.txt
        S3:
            users/1/file.txt
        MinIO:
            users/1/file.txt

        """
        pass

    @abstractmethod
    def open(
        self,
        path,
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
