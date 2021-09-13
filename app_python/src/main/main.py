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
logger_names = ['waitress', 'wsgi']
loggers = [logging.getLogger(name) for name in logger_names]

if os.environ['MODE'] == 'PROD':
    for logger in loggers:
        logger.setLevel(logging.INFO)
    serve(TransLogger(app, loggers[1]), port=5000)
