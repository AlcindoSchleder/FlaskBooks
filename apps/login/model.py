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
        developer   : Alcindo Schleder
        version     : 1.0.0
        test version: 1
        test status :
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

    def __init__(self, pkUser=None, Username=None, Login=None, Passwd=None, dateUpdate=None,
                 dateInsert=None):
        self.pk_user = pkUser if pkUser else None
        self.username = Username if Username else None
        self.login = Login if Login else None
        self.passwd = Passwd if Passwd else 0
        self.date_update = dateUpdate
        self.date_insert = dateInsert if dateInsert else datetime.now()

    def gen_hash(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)

    @validates('passwd', include_backrefs=False)
    def passwd(self, key, address):
        assert ((address > -1) and (address < 6)), "Field 'flag_tcat' only supports value between 0 and 5!"
        return address

    @property
    def tableName(self):
        return self.__tablename__