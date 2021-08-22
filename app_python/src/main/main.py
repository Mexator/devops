from flask import Flask

from src.main import config
from src.main import routes

app = Flask(config.app_name)
routes.init_routes(app)
