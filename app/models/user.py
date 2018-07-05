# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/5 00:05
"""
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import NotFoundException, AuthException
from app.models.base import Base, db

__author__ = 'Cphayim'


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(32), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        """
        核验账号
        :param email: email
        :param password: 密码
        :return:
        """
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise AuthException()

        return {'uid': user.id, 'scope': ''}

    def check_password(self, raw):
        """
        确认密码
        :param raw:
        :return:
        """
        if not self._password:
            return False
        return check_password_hash(self._password, raw)
