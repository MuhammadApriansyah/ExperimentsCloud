"""
Utilities for file formatting.
"""


def human_size(size: int) -> str:
    """
    Convert bytes into a human-readable string.
    """

    units = (
        "B",
        "KB",
        "MB",
        "GB",
        "TB",
    )

    size = float(size)

    for unit in units:

        if size < 1024 or unit == units[-1]:
            return f"{size:.1f} {unit}" if unit != "B" else f"{int(size)} B"

        size /= 1024
