# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/4 20:16
"""
from flask import Blueprint

from app.api.v1 import book, user

__author__ = 'Cphayim'


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__, url_prefix='/v1')
    a =bp_v1.url_prefix
    # 注册红图
    book.api.register(bp_v1)
    user.api.register(bp_v1)
    return bp_v1
