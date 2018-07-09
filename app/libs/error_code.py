# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/5 11:37
"""
from app.libs.enums import HTTPStatusCode
from app.libs.error import APIException

__author__ = 'Cphayim'


# 200 查询成功
# 201 创建(更新)成功
# 204 删除成功

# 400 参数错误
# 401 未授权
# 403 禁止访问
# 404 没有找到资源

# 500 服务器未知错误

class Success(APIException):
    """
    提交(POST/PUT)成功
    """
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    """
    删除(DELETE)成功
    """
    # 这里不使用标准 RESTFul 中规定的 204 状态码，因为 204 状态码不会携带任何响应体
    # 为便于前端判断，这里使用 code 为 202，error_code 为 1 表示删除成功
    code = 202
    error_code = 1


class ParameterException(APIException):
    """
    参数错误异常
    """
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class AuthException(APIException):
    """
    授权异常
    """
    code = 401
    msg = 'authorization failed'
    error_code = 1005


class NotFoundException(APIException):
    """
    找不到资源异常
    """
    code = 404
    msg = 'the resource are not_found 0__0...'
    error_code = 1001


class ServerException(APIException):
    """
    服务器未知异常
    """
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999

# class ClientTypeError(APIException):
#     code = 400
#     msg = 'client is invalid'
#     error_code = 1006
