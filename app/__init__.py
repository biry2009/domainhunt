from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask import Blueprint

main = Blueprint('main', __name__)
registrar = Blueprint('registrar', __name__)

moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .registrar import registrar as registrar_blueprint
    app.register_blueprint(registrar_blueprint)

    return app
