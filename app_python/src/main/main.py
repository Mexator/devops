"""Entrypoint of application"""
import os
import logging
from flask import Flask
from waitress import serve
from paste.translogger import TransLogger

from src.main import config
from src.main import routes

app = Flask(config.app_name)
routes.init_routes(app)

logging.basicConfig()
accessLogger = logging.getLogger('wsgi')
accessLogger.addHandler(logging.FileHandler('access.log'))
accessLogger.setLevel(logging.INFO)

if os.environ['MODE'] == 'PROD':
    app = TransLogger(app, accessLogger, setup_console_handler=False)
    serve(app, port=5000)
