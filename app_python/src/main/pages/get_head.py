"""Methods for generating <head> tag for pages"""
from src.main.config import app_name
from src.main.pages import env

def get_head():
    """Return head of every html page"""
    head = env.get_template("head.html")
    return head.render(title=app_name)
