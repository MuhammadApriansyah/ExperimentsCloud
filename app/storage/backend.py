from abc import ABC, abstractmethod


class StorageBackend(ABC):

    @abstractmethod
    def key(
        self,
        user_id,
        stored_name,
    ):
        pass

    @abstractmethod
    def resolve(
        self,
        path,
    ):
        pass

    @abstractmethod
    def file_path(
        self,
        user_id,
        stored_name,
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
