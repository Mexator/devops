"""Module, where application routes are defined"""
from flask import Flask

from src.main.pages.get_clock_page import get_page


def init_routes(app: Flask):
    """Adds routes listeners to `app`"""

    @app.route('/')
    def clock_route():
        return get_page()
