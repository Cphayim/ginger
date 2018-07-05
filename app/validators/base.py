# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/5 14:03
"""
from flask import request
from flask_wtf import Form

from app.libs.error_code import ParameterException

__author__ = 'Cphayim'


class BaseForm(Form):

    def __init__(self, data=None):
        # 如果外部没有传入 data，从 request 中获取请求参数
        if not data:
            data = request.json
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        """
        验证器
        替代父类的 validate() 方法供外部调用
        返回 self
        若验证失败将抛出一个带验证错误信息的 ParameterException
        :return:
        """
        valid = super(BaseForm, self).validate()
        if not valid:
            """
            调用 Form 的 validate() 后，所有的异常信息会保存在 form.error 中
            这里需要将它传入 PrameterException() 中抛出
            """
            raise ParameterException(msg=self.errors)

        return self
