def format_file_size(size):

    if size < 1024:
        return f"{size} B"

    if size < 1024 * 1024:
        return f"{size // 1024} KB"

    return (
        f"{size // (1024 * 1024)} MB"
    )

def get_file_icon(extension):

    icons = {
        "pdf": "📄",
        "txt": "📝",
        "jpg": "🖼",
        "jpeg": "🖼",
        "png": "🖼",
        "gif": "🖼",
        "mp3": "🎵",
        "wav": "🎵",
        "mp4": "🎬",
        "avi": "🎬",
        "zip": "📦",
        "rar": "📦",
    }

    return icons.get(
        extension.lower(),
        "📁",
    )


def get_file_type(extension):

    types = {
        "pdf": "PDF Document",
        "txt": "Text File",
        "jpg": "JPEG Image",
        "jpeg": "JPEG Image",
        "png": "PNG Image",
        "gif": "GIF Image",
        "mp3": "MP3 Audio",
        "wav": "WAV Audio",
        "mp4": "MP4 Video",
        "avi": "AVI Video",
        "zip": "ZIP Archive",
        "rar": "RAR Archive",
    }

    return types.get(
        extension.lower(),
        "Unknown File",
    )
