def format_file_size(size):

    if size < 1024:
        return f"{size} B"

    if size < 1024 * 1024:
        return f"{size // 1024} KB"

    return (
        f"{size // (1024 * 1024)} MB"
    )
