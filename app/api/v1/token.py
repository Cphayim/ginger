# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/5 17:12
"""
from flask import current_app, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientTypeForm

__author__ = 'Cphayim'

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientTypeForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )
    expiration = current_app.config.get('TOKEN_EXPIRATION')
    token = generate_auth_token(
        identity['uid'],
        form.type.data,
        identity['scope'],
        expiration
    )
    t = {'token': token.decode('ascii')}
    return jsonify(t)


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """
    生成令牌
    :param uid: 用户 id
    :param ac_type: 客户端类型
    :param scope: 权限作用域
    :param expiration: 有效期
    :return:
    """
    s = Serializer(
        current_app.config['SECRET_KEY'],
        expires_in=expiration
    )
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,  # 枚举值.value
        'scope': scope
    })
