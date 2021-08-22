"""Methods for generating <head> tag for pages"""
import config
import pages

def get_head():
    """Return head of every html page"""
    head = pages.env.get_template("head.html")
    return head.render(title=config.app_name)
