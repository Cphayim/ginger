# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/4 20:17
"""
from flask import jsonify, g

from app.libs.error_code import NotFoundException, DeleteSuccess, AuthException
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

__author__ = 'Cphayim'

api = Redprint('user', url_prefix='/user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    """
    查询用户
    :param uid: 用户 id
    :return:
    """
    user = User.query.get_or_404(uid)
    return jsonify(user)


# @api.route('', methods=['DELETE'])
# @auth.login_required
# def delete_user():
#     """
#     删除用户
#     :param uid: 用户 id
#     :return:
#     """
#     # 防止超权，用户只能删除自己
#     uid = g.user.uid
#     with db.auto_commit():
#         user = User.query.filter_by(id=uid).first_or_404()
#         user.delete()
#     return DeleteSuccess()

# 保持 API 格式统一的另一种写法
@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def delete_user(uid):
    # 防止超权，用户只能删除自己
    current_uid = g.user.uid
    if uid != current_uid:
        raise AuthException()
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route('/<int:uid>', methods=['UPDATE'])
def update_user():
    return 'delete user'

# @api.route('/<int:uid>', methods=['DELETE'])
# def delete_user():
#     return 'delete user'
