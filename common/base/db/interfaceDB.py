# -*- coding: utf-8 -*-
import common.helpers.exceptions as company_exceptions
from common.helpers.operation_results import OperationResults

""" 
    vars        : Constants Definitions
    descritption: Constants defintion for Users Permitions
    author      : Alcindo Schleder
    version     : 1.0.0
    package     : i-City Identification Plataform
"""
FLAG_BROWSE = 0x0001
FLAG_INSERT = 0x0002
FLAG_UPDATE = 0x0004
FLAG_DELETE = 0x0008

ADMIN_PERM = (FLAG_BROWSE & FLAG_INSERT & FLAG_UPDATE & FLAG_DELETE)
CLIENT_PERM = (FLAG_BROWSE & FLAG_INSERT & FLAG_UPDATE)
WRITE_PERM = (FLAG_BROWSE & FLAG_INSERT)
UPDATE_PERM = (FLAG_BROWSE & FLAG_UPDATE)
READ_PERM = FLAG_BROWSE

DSC_PERM = { 
    FLAG_BROWSE: 'Read',
    FLAG_INSERT: 'Insert',
    FLAG_UPDATE: 'Edit',
    FLAG_DELETE: 'Delete',
    ADMIN_PERM: 'Administrator',
    CLIENT_PERM: 'Client'
}


class DBOperations:
    """
        class       : DBOperations
        Description : Define all Permissions to user manage database tables (CRUD)
        version     : 1.0.0
        Developer   : Alcindo Schleder
        package     : i-City Identification Plataform
    """

    def __init__(self):
        pass

    @staticmethod
    def get_valid_permissions():
        return [
            ADMIN_PERM, 
            CLIENT_PERM, 
            WRITE_PERM, 
            UPDATE_PERM,
            READ_PERM
        ]


class IDatabases(OperationResults, DBOperations):
    """
        class       : IDatabases (Interface)
        Description : Basic CRUD Database class to use as Interface
        version     : 1.0.0
        Developer   : Alcindo Schleder
        package     : i-City Identification Plataform
    """
    _db = None
    _session = None
    _model = None
    _DATABASE_URI = None

    def __init__(self):
        super(IDatabases, self).__init__()
        self._valid_permissions = self.get_valid_permissions()
        self._user_permission = READ_PERM
        self._db = None
        self._session = None
        self._model = None
        self._DATABASE_URI = None

    def _set_driver(self, driver: str):
        raise NotImplementedError()

    def _config_db(self):
        raise NotImplementedError()

    def _create_session(self):
        raise NotImplementedError()

    def connect(self):
        raise NotImplementedError()

    def disconnect(self):
        raise NotImplementedError()

    @property
    def is_connected(self):
        if self._session is None:
            Exception(company_exceptions.NotInitializedSession)
        return bool(self._session is not None and self._session.is_active)

    @property
    def db(self):
        return self._session

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, table):
        self._model = table

    @property
    def table_name(self) -> str:
        return self._model.table_name

    # @property
    # def engine(self):
    #     return self._engine

    # @property
    # def session(self):
    #     return self._session

    def _can_exec(self, permission):
        return self._user_permission & permission

    def exec_command(self, query: str, params: dict = None):
        raise NotImplementedError()

    def browse_record(self, **parameters):
        if self.__class__.__name__ == 'IDatabases':
            raise NotImplementedError()
        if not self._can_exec(FLAG_BROWSE):
            raise company_exceptions.UserNotHasPermission(DSC_PERM[FLAG_BROWSE])

    def insert_record(self):
        if self.__class__.__name__ == 'IDatabases':
            raise NotImplementedError()
        if not self._can_exec(FLAG_INSERT):
            raise company_exceptions.UserNotHasPermission(DSC_PERM[FLAG_INSERT])

    def update_record(self):
        if self.__class__.__name__ == 'IDatabases':
            raise NotImplementedError()
        if not self._can_exec(FLAG_UPDATE):
            raise company_exceptions.UserNotHasPermission(DSC_PERM[FLAG_UPDATE])

    def delete_record(self):
        if self.__class__.__name__ == 'IDatabases':
            raise NotImplementedError()
        if not self._can_exec(FLAG_DELETE):
            raise company_exceptions.UserNotHasPermission(DSC_PERM[FLAG_DELETE])

    def set_permission(self, new_permission: int = READ_PERM):
        if self.__class__.__name__ == 'IDatabases':
            raise NotImplementedError()
        if new_permission not in self._valid_permissions:
            raise company_exceptions.InvalidPermissionException(new_permission)
