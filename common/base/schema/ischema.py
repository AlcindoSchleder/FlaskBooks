# -*- coding: utf-8 -*-
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declared_attr, as_declarative


@as_declarative()
class SchemaBase:
    """
        class       : SchemaBase
        description : Base Class to init all schema classes
        version     : 1.0.0
        developer   : Alcindo Schleder
    """

    __name__ = None

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()

    def as_dict(self):
        return {
            c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs
        }

    def __repr__(self):
        s = f'<{self.__tablename__}('
        for c in inspect(self).mapper.column_attrs:
            s += f'{c.key}={getattr(self, c.key)}, '
        s = s[:len(s) - 2] + ')>'
        return s
