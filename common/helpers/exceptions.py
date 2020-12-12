# -*- coding: utf-8 -*-
class ErrorUnexpectedEndPointResult(Exception):
    """
        class       : ErrorUnexpectedEndPointResult
        description : Exceção reportada quando não se consegue abrir um
                      EndPoint ou retornou um json inesperado
        developer   : Alcindo Schleder
        version     : 1.0.0
    """
    def __init__(self, end_point: str, data: dict):
        _msg = f'Resultado do EndPoint {end_point} iválido!\n {data}'
        super(ErrorUnexpectedEndPointResult, self).__init__(_msg)


class UserNotHasPermission(Exception):
    """
        class       : UserNotHasPermission
        description : Exception if session DB is not initialized
        developer   : Alcindo Schleder
        version     : 1.0.0
    """
    def __init__(self, permission_name: str):
        _msg = f'User has not permission to execute %s db operation! {permission_name}'
        super(UserNotHasPermission, self).__init__(_msg)


class InvalidPermissionException(Exception):
    """
        class       : UserNotHasPermission
        description : Exception for user permissions
        developer   : Alcindo Schleder
        version     : 1.0.0
    """
    def __init__(self, permission: int = 0):
        _msg = f'Attempting to assign an invalid user permission ({permission})! '
        super(InvalidPermissionException, self).__init__(_msg)


class NotInitializedSession(Exception):
    """
        class       : UserNotHasPermission
        description : Exception if session DB is not initialized
        developer   : Alcindo Schleder
        version     : 1.0.0
    """
    def __init__(self):
        _msg = 'Session not initialized for any database!'
        super(NotInitializedSession, self).__init__(_msg)


class HttpCodeNotFound(Exception):
    """
        class       : UserNotHasPermission
        description : Exception when HTTPD code on result is invalid
        developer   : Alcindo Schleder
        version     : 1.0.0
    """
    def __init__(self, code):
        _msg = f'Http code {code} not found on list of http_codes!'
        super(HttpCodeNotFound, self).__init__(_msg)


class HttpTemplateNotFound(Exception):
    """
        class       : UserNotHasPermission
        description : Exception if application view not found a template
        developer   : Alcindo Schleder
        version     : 1.0.0
    """
    def __init__(self, template):
        if template is None:
            template = '<None>'
        _msg = f'Http template {template} not found!'
        super(HttpTemplateNotFound, self).__init__(_msg)
