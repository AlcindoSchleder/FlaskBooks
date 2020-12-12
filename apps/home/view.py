# -*- coding: utf-8 -*-
import random
import json
import time
from flask_fontawesome import FontAwesome
from common.base.routes.iview_routes import IViewRoutes, APP_BASE_NAME
from server import server
from server.company_server import log


class HomeRoute(IViewRoutes):
    """
        class       : HomeRoute
        description : Root Route of Application
        developer   : Alcindo Schleder
        version     : 1.0.0
        test version: 1
        test status : passed
    """

    list_images = None

    def dispatch_request(self):
        self.template_name = 'home/index.html'
        # self.user_context =
        log.info('Request GET at /')
        return super(HomeRoute, self).dispatch_request()


api_functions = HomeRoute.as_view(APP_BASE_NAME)
server.server_app.add_url_rule('/', view_func=api_functions, methods=['GET'])

fa = FontAwesome(server.server_app)
