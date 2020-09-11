from flask_restful import Api
from flask_pdv.ext.resources.transacao import Transacao


def init_app(app):
    api = Api(app, prefix="/api/v1")

    api.add_resource(Transacao, "/transacao")