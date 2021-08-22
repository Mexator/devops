from flask import Flask

import config
import routes

app = Flask(config.app_name)
routes.init_routes(app)