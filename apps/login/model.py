# -*- coding: utf-8 -*-
from datetime import datetime
from passlib.hash import pbkdf2_sha256

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import validates
from common.base.schema.ischema import SchemaBase


class Users(SchemaBase):
    """
        class       : Users model
        description : Model of table to login
        version     : 1.0.0
        developer   : Alcindo Schleder <alcindoschleder@gmail.com>
    """

    __tablename__ = 'users'
    # __filters__   = None

    pk_user = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    username = Column(String(100), nullable=False)
    login = Column(String(50), nullable=False)
    passwd = Column(String(255), nullable=False)
    update_date = Column(DateTime, nullable=False)
    insert_date = Column(DateTime, nullable=True)

    def __init__(self, pkUser=None, Username=None, eMail=None, Login=None, Passwd=None, updateDate=None,
                 insertDate=None):
        self.pk_user = pkUser
        self.username = Username
        self.eMail = eMail
        self.login = Login
        self.passwd = Passwd
        self.update_date = updateDate
        self.insert_date = insertDate if insertDate else datetime.now()

    def gen_hash(self):
        return pbkdf2_sha256.hash(self.password)

    def verify_password(self, passwd):
        return pbkdf2_sha256.verify(passwd, self.passwd)

    @validates('passwd', include_backrefs=False)
    def passwd(self, key, address):
        assert ((address > -1) and (address < 6)), "Field 'Senha' must has 6 or more chars!"
        address = self.gen_hash()
        return address

    @property
    def tableName(self):
        return self.__tablename__
