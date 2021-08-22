"""This module contains tests for the project. Can be split into several files
later"""

from datetime import datetime
import pytz

from src.main.pages.get_clock_page import get_time_str

zone = pytz.timezone("Europe/Moscow")


def test_time_gen():
    "Test for generation of time widget content"
    expected = '''
Sunday, 22 August 2021
16:53:57
'''

    def get_time():
        return datetime.fromtimestamp(1629629637)

    result = get_time_str(timezone=zone, get_utc_time=get_time)
    if result != expected:
        raise Exception("test failed")


if __name__ == '__main__':
    test_time_gen()
