from app.storage.key_builder import StorageKeyBuilder


def test_user_file_key():

    key = StorageKeyBuilder.user_file(
        10,
        "hello.txt",
    )

    assert key == "users/10/hello.txt"
