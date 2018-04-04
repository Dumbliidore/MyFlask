# -*-coding:utf-8-*-

__Author__ = "Mr.D"
__Date__ = '2018\4\1 0001 22:15'

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    #初始化配置文件
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # 这一句必须放在db.init_app(app)之下
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app




