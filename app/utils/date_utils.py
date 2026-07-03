"""
Utilities for date formatting.
"""

from datetime import datetime


def human_datetime(value: datetime) -> str:

    return value.strftime(
        "%d %b %Y %H:%M"
    )
