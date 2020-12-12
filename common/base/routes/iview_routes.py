# -*- coding: utf-8 -*-
from flask import render_template, render_template_string
from flask.views import View
from common.helpers.operation_results import OperationResults
from common.helpers.exceptions import HttpTemplateNotFound
from server import server

APP_ROOT = server.server_prefix
APP_BASE_NAME = 'home'
VERSION = '1.0'
PREFIX_ROUTE = f'{APP_ROOT}/{APP_BASE_NAME}'
PATH_APP = f'{APP_ROOT}/{APP_BASE_NAME}'


class IViewRoutes(View, OperationResults):
    """
        class       : IViewRoutes (Interface)
        description : Class that manage class based views resulting on string or html template
        version     : 1.0.0
        developer   : Alcindo Schleder
    """
    template_name = None
    user_context = None
    db = None

    def __init__(self, *args, **kwargs):
        super(IViewRoutes, self).__init__(args, kwargs)
        self.db = None

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
                obj_len=0
                # Se o contexto é um objeto to tipo <class list> envia o tamanho do lista no contexto
                if isinstance(data, list):
                    obj_len = len(data)
                return render_template(self.get_template_name(), len=obj_len, data=data), self.status_code
