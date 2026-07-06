from pathlib import Path

from app.storage.local import LocalStorage


def test_local_storage_exists(tmp_path):

    storage = LocalStorage(tmp_path)

    file = tmp_path / "hello.txt"

    file.write_text("hello")

    storage.save(file, "saved.txt")

    assert storage.exists("saved.txt")
