# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask_restplus import reqparse
from common.helpers.operation_results import OperationResults
from server import server

APP_ROOT = server.server_prefix
APP_BASE_NAME = 'home'
VERSION = '1.0'
PREFIX_ROUTE = f'{APP_ROOT}/{APP_BASE_NAME}'
PATH_API = f'{APP_ROOT}/{APP_BASE_NAME}/{VERSION}'


class IApiRoutes(MethodView, OperationResults):
    """
        class       : IApiRoutes (Interface)
        description : Class that manage class based views restfull api
        version     : 1.0.0
        developer   : Alcindo Schleder
    """

    PAGE = reqparse.RequestParser()
    PAGE.add_argument(
        'start',
        type=int,
        default=1,
        help='Página inicial da lista'
    )
    PAGE.add_argument(
        'limit', 
        type=int, 
        default=20, 
        help='Registros por paǵina', 
        choices=[0, 10, 20, 30, 40, 50]
    )

    db = None

    def __init__(self, *args, **kwargs):
        super(IApiRoutes, self).__init__(args, kwargs)
        self.result['page'] = {
            'count': 0,
            'start': 0,
            'limit': 0,
            'url': '/'
        }
        self.db = None

    def get(self):
        raise NotImplementedError()
