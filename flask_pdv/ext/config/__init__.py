


def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///api.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = 'secret'