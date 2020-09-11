from flask_restful import Resource, marshal
from flask_pdv.ext.api import requests
from flask_pdv.ext.db.models import TransacaoModel
from flask_pdv.ext.db.schemas import transacao_field
from flask_pdv.ext.db import db



class Transacao(Resource):
    def get(self):
        transacao = TransacaoModel.query.all()
        return marshal(transacao, transacao_field)


    def post(self):
        payload = requests.only(["estabelecimento", "cliente", "valor", "descricao"])
        transacao = TransacaoModel()
        
        transacao.estabelecimento = payload["estabelecimento"]
        transacao.cliente = payload["cliente"]
        transacao.valor = payload["valor"]
        transacao.descricao = payload["descricao"]

        db.session.add(transacao)
        db.session.commit()

        return {"aceito": True}

    def put(self):
        ...
    
    def delete(self):
        ...
