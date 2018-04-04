# -*-coding:utf-8-*-

__Author__ = "Mr.D"
__Date__ = '2018\4\1 0001 22:18'

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
