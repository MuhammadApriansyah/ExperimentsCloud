from pathlib import PurePosixPath


class StorageKeyBuilder:

    @staticmethod
    def user_directory(
        user_id: int,
    ) -> str:
        return str(
            PurePosixPath(
                "users",
                str(user_id),
            )
        )

    @staticmethod
    def user_file(
        user_id: int,
        stored_name: str,
    ) -> str:
        return str(
            PurePosixPath(
                StorageKeyBuilder.user_directory(
                    user_id,
                ),
                stored_name,
            )
        )
