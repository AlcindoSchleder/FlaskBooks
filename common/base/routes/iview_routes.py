# -*- coding: utf-8 -*-
from flask import render_template, render_template_string
from flask.views import MethodView, View, request
from common.base.db.connection import Connection
from common.helpers.operation_results import OperationResults
from common.helpers.exceptions import HttpTemplateNotFound
from server import server

APP_ROOT = server.server_prefix
APP_BASE_NAME = 'home'
VERSION = '1.0'
PREFIX_ROUTE = f'{APP_ROOT}/{APP_BASE_NAME}'
PATH_APP = f'{APP_ROOT}/{APP_BASE_NAME}'


class ICRUDRoutes(MethodView, OperationResults):
    """
    class       : ICRUDRoutes (Interface)
    description : Class that manage views to handle database
    version     : 1.0.0
    developer   : Alcindo Schleder
    """
    _db = None
    _model = None
    pk = None
    context = None
    template = None

    def __init__(self, *args, **kwargs):
        super(ICRUDRoutes, self).__init__(args, kwargs)
        self._db = Connection(server.server_app)
        self.context = kwargs.get('context', None)
        self.template = kwargs.get('template', None)

    def __del__(self):
        self._db.close()

    def get_template_name(self) -> str:
        """
        Function that returns a name of template defined on __int__() of main view
        @rtype: str
        """
        if self.template is None:
            raise HttpTemplateNotFound
        return self.template

    def get_queryset(self):
        pass

    def get(self, *args, **kwargs):
        filters = kwargs.get('filters', None)
        if filters is not None and type(filters) != dict:
            filters = None
        return self._db.browse_record(**filters)

    def post(self, *args, **kwargs):
        return self._db.insert_record()

    def update(self, *args, **kwargs):
        return self._db.update_record()

    def delete(self, *args, **kwargs):
        return self._db.delete_record()

    def dispatch_request(self, *args, **kwargs):
        """
        result a data that will be showed on browser
        @return: Any
        """
        self.status_code = 200
        data = None
        meth = getattr(self, request.method.lower(), None)
        if self.template is None and self.context is None and meth == 'get':
            self.context = 'Hello World! Nothing to show on this page!'
            return render_template_string(self.context), self.status_code
        # data data from database
        self.context = super(ICRUDRoutes, self).dispatch_request(args, kwargs)
        obj_len = 0
        if isinstance(self.context, dict):
            obj_len = 0 if self.context.get('records', None) is None \
                else len(self.context['records'])

        return render_template(
            self.get_template_name(), len=obj_len, data=self.context
        ), self.status_code


class IViewRoutes(View, OperationResults):
    """
    class       : IViewRoutes (Interface)
    description : Class that manage class based views resulting on string or html template
    version     : 1.0.0
    developer   : Alcindo Schleder
    """
    template_name = None
    user_context = None

    def __init__(self, *args, **kwargs):
        super(IViewRoutes, self).__init__(args, kwargs)

    def get_template_name(self) -> str:
        """
        Function that returns a name of template defined on __int__() of main view
        @rtype: str
        """
        if self.template_name is None:
            raise HttpTemplateNotFound
        return self.template_name

    def dispatch_request(self):
        """
        result a data that will be showed on browser
        @return: Any
        """
        self.status_code = 200
        data = None
        if self.template_name is None and self.user_context is None:
            data = 'Hello World! Nothing to show on this page!'
        if self.template_name is None:
            return render_template_string(data), self.status_code
        else:
            data = self.user_context
            if self.user_context is None:
                return render_template(self.get_template_name()), self.status_code
            else:
                self.user_context = None
                obj_len = 0
                # Se o contexto é um objeto to tipo <class list> envia o tamanho do lista no contexto
                if isinstance(data, list):
                    obj_len = len(data)
                return render_template(self.get_template_name(), len=obj_len, data=data), self.status_code
