from flask import Flask

import pages.get_clock_page as get_clock_page

def init_routes(app: Flask):

    @app.route('/')
    def clock_route():
        return get_clock_page.get_page()