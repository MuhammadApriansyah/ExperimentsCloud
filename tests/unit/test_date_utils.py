from datetime import datetime

from app.utils.date_utils import human_datetime


def test_human_datetime():

    value = datetime(
        2026,
        7,
        4,
        13,
        30,
    )

    assert human_datetime(
        value
    ) == "04 Jul 2026 13:30"


def test_human_datetime_midnight():

    value = datetime(
        2026,
        1,
        1,
        0,
        0,
    )

    assert human_datetime(
        value
    ) == "01 Jan 2026 00:00"


def test_human_datetime_return_type():

    value = datetime.now()

    assert isinstance(
        human_datetime(value),
        str,
    )
