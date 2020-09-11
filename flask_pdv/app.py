from flask import Flask

from flask_pdv.ext import db
from flask_pdv.ext import config
from flask_pdv.ext import migrate
from flask_pdv.ext import api
from flask_pdv.ext import cli



def create_app():
    app = Flask(__name__)

    config.init_app(app)
    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)

    return app