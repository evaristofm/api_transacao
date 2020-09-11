from flask_migrate import Migrate
from flask_pdv.ext.db import db
from flask_pdv.ext.db import models 


migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)