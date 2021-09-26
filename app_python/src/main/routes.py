"""Module, where application routes are defined"""
from flask import Flask, send_file
import logging
import os

from src.main.pages.get_clock_page import get_page

def init_routes(app: Flask, logpath: str):
    """Adds routes listeners to `app`"""

    @app.route('/')
    def clock_route():
        return get_page()

    @app.route('/visits')
    def access_logs():
        return send_file(logpath + 'access.log')
