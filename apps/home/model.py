# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime, ForeignKey, inspect
from sqlalchemy.orm import validates
from common.base.schema.ischema import SchemaBase


class Categories(SchemaBase):
    """
        Class that define the user table
        * class      User
        * requires   python 3.5+
        * version    1.0.0
        * package    icity-BlockChain
        * author     Alcindo Schleder <alcindoschleder@gmail.com>
        * copyright  Vocatio Telecom <https://www.vocatiotelecom.com.br>
    """
    __tablename__ = 'categories'
    # __filters__   = None

    pk_categories = Column(Integer, primary_key=True)
    dsc_tcat = Column(String(100), nullable=False)
    flag_tcat = Column(Integer, nullable=False, default=TTypeRoles.trUsers)
    flag_default = Column(Integer, nullable=False, default=0)
    date_update = Column(DateTime, nullable=True)
    date_insert = Column(DateTime, nullable=False)

    def __init__(self, pkCategories=None, dscTCat=None, flagTCat=None, flagDefault=None, dateUpdate=None,
                 dateInsert=None):
        self.pk_categories = pkCategories if (pkCategories) else 0
        self.dsc_tcat = dscTCat if (dscTCat) else ' '
        self.flag_tcat = flagTCat if (flagTCat) else 0
        self.flag_default = flagDefault if (flagDefault) else 0
        self.date_update = dateUpdate
        self.date_insert = dateInsert if (dateInsert) else datetime.now()

    @validates('flag_tcat', include_backrefs=False)
    def validate_flag_tcat(self, key, address):
        assert ((address > -1) and (address < 6)), "Field 'flag_tcat' only supports value between 0 and 5!"
        return address

    @validates('flag_default', include_backrefs=False)
    def validate_flag_default(self, key, address):
        assert (address in (0, 1)), "Field 'flag_default' only accept false(0) or true(1)!"
        return address

    @property
    def tableName(self):
        return self.__tablename__