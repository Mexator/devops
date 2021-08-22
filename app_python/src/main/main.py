"""Entrypoint of application"""
import os
from flask import Flask
from waitress import serve

from src.main import config
from src.main import routes

app = Flask(config.app_name)
routes.init_routes(app)

if os.environ['MODE'] == 'PROD':
    serve(app, port=5000)
