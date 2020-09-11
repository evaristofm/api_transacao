from . import db


class TransacaoModel(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    estabelecimento = db.Column(db.String(30) , nullable=False)
    cliente = db.Column(db.String(30), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.Text, nullable=True)