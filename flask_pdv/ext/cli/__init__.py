from flask_pdv.ext.db import db


def init_app(app):
    @app.cli.command()
    def create_db():
        """ Criando o DB """
        db.create_all()