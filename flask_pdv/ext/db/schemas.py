from flask_restful import fields

transacao_field = {
    "estabelecimento": fields.String,
    "cliente": fields.String,
    "valor": fields.Float,
    "descricao":fields.String
}