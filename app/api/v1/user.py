# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/4 20:17
"""
from app.libs.redprint import Redprint

__author__ = 'Cphayim'

api = Redprint('user', url_prefix='/user')


@api.route('/get')
def get_user():
    return 'I am Cphayim.'
