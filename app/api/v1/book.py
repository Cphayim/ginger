# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/4 20:17
"""
from app.libs.redprint import Redprint

__author__ = 'Cphayim'

api = Redprint('book', url_prefix='/book')


@api.route('/get')
def get_book():
    return 'get book'


@api.route('/create')
def create_book():
    return 'create book'
