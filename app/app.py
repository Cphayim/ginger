# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/4 18:24
"""
from flask import Flask

__author__ = 'Cphayim'


def create_app():
    """
    创建 app
    :return:
    """
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprint(app)

    return app


def register_blueprint(app):
    """
    注册蓝图
    :param app: Flask core
    :return:
    """
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1())
