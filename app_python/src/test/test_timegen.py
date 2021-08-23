"""This module contains tests for the project. Can be split into several files
later"""

from datetime import datetime
import pytest
import pytz

from src.main.pages.get_clock_page import get_time_str

zone = pytz.timezone("Europe/Moscow")

@pytest.mark.parametrize(
    ('freeze_ts', 'expected_res'),
    [
        (1629629637, 'Sunday, 22 August 2021\n13:53:57'),
    ]
)
def test_time_gen(freezer, freeze_ts, expected_res):
    "Test for generation of time widget content"
    freezer.move_to(datetime.fromtimestamp(freeze_ts))

    result = get_time_str(timezone=zone)
    assert result == expected_res
