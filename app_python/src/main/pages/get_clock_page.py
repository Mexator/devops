"""Page provider for clock page"""
from datetime import datetime
import pytz

import config
import pages.get_head as get_head
import pages

_clock_zone = pytz.timezone(config.clock_zone)
_FORMAT = '''
%A, %d %B %Y
%H:%M:%S
'''

def get_time_str(get_utc_time = datetime.utcnow):
    """Return current date and time string, zoned with timezone from config"""
    # datetime is zoned as UTC
    time = pytz.utc.localize(get_utc_time())
    # change TZ to required one
    localized = time.astimezone(_clock_zone)
    return localized.strftime(_FORMAT)


def get_page():
    """Return page with clock"""
    template = pages.env.get_template("clock.html")
    rendered = template.render(time = get_time_str())
    return get_head.get_head() + rendered
