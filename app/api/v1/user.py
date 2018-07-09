# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/4 20:17
"""
from flask import jsonify

from app.libs.error_code import NotFoundException
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User

__author__ = 'Cphayim'

api = Redprint('user', url_prefix='/user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    return jsonify(user)
