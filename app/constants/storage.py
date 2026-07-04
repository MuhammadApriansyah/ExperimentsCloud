from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

STORAGE_ROOT = BASE_DIR / "storage"

USER_STORAGE = STORAGE_ROOT / "users"

TEMP_STORAGE = STORAGE_ROOT / "temp"

THUMBNAIL_STORAGE = STORAGE_ROOT / "thumbnails"

TRASH_STORAGE = STORAGE_ROOT / "trash"

MAX_UPLOAD_SIZE = 100 * 1024 * 1024

ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "gif",
    "pdf",
    "txt",
    "doc",
    "docx",
    "xls",
    "xlsx",
    "ppt",
    "pptx",
    "zip",
    "rar",
}
