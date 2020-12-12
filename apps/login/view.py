# -*- coding: utf-8 -*-
import random
import json
import time
from flask_fontawesome import FontAwesome
from common.base.routes.iview_routes import IViewRoutes, APP_BASE_NAME
from server import server
from server.company_server import log


class LoginRoute(IViewRoutes):
    """
        class       : LoginRoute
        description : Route and Page for CRUD Users
        developer   : Alcindo Schleder
        version     : 1.0.0
        test version: 1
        test status :
    """

    list_images = None

    def dispatch_request(self):
        self.template_name = 'login/index.html'
        # self.user_context =
        log.info('Request GET at /login')
        return super(LoginRoute, self).dispatch_request()


api_functions = LoginRoute.as_view(APP_BASE_NAME)
server.server_app.add_url_rule('/login', view_func=api_functions, methods=['GET'])
