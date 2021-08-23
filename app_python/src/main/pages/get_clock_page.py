"""Page provider for clock page"""
from datetime import datetime
import pytz

from src.main.pages import env
from src.main.config import clock_zone
from src.main.pages.get_head import get_head

_clock_zone = pytz.timezone(clock_zone)
_FORMAT = '''%A, %d %B %Y\n%H:%M:%S'''


def get_time_str(timezone=_clock_zone):
    """Return current date and time string, zoned with timezone from config"""
    get_utc_time=datetime.utcnow
    # datetime is zoned as UTC
    time = pytz.utc.localize(get_utc_time())
    # change TZ to required one
    localized = time.astimezone(timezone)
    return localized.strftime(_FORMAT)


def get_page():
    """Return page with clock"""
    template = env.get_template("clock.html")
    rendered = template.render(time=get_time_str())
    return get_head() + rendered
