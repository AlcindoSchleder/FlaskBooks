# -*- coding: utf-8 -*-
from datetime import datetime
from flask_restplus import reqparse
from common.base.routes.iview_routes import ICRUDRoutes, IViewRoutes, APP_BASE_NAME
from server import server
from server.company_server import log
from .model import Users
from .serializer import UsersSerializer

page_parser = reqparse.RequestParser()
page_parser.add_argument('page', type=int, default=1, help='Página da lista')

class RegisterUsersRoute(ICRUDRoutes):
    """
    class       : RegisterUsersRoute
    description : Route to register user
    version     : 1.0.0
    developer   : Alcindo Schleder <alcindoschleder@gmail.com>
    """
    model = Users
    template = 'login/register.html'

    def get(self, pk: int = 0):
        return super(RegisterUsersRoute, self).get(pk=pk)

    def post(self, data: dict):
        data['update_date'] = None
        data['insert_date'] = datetime.now()
        self.model = Users(
            Username=data['Username'],
            eMail=data['eMail'],
            Login=data['Login'],
            Passwd=data['Passwd'],
            updateDate=data['updateDate'],
            insertDate=data['insertDate']
        )
        return super(RegisterUsersRoute, self).post()

    def update(self, data: dict):
        self.model = Users(
            pkUser=data['pkUser'],
            eMail=data['eMail'],
            Login=data['Login'],
            Passwd=data['Passwd'],
            updateDate=data['updateDate'],
            insertDate=data['insertDate']
        )
        return super(RegisterUsersRoute, self).update()

    def delete(self, pk: int):
        self.model = Users(pkUser=pk)
        return super(RegisterUsersRoute, self).delete()


class LoginRoute(IViewRoutes):
    """
        class       : LoginRoute
        description : Route to login on system
        version     : 1.0.0
        developer   : Alcindo Schleder <alcindoschleder@gmail.com>
    """

    def dispatch_request(self):
        self.template_name = 'login/login.html'
        # self.user_context =
        log.info('Request GET at /login')
        return super(LoginRoute, self).dispatch_request()


class LogoutRoute(IViewRoutes):
    """
    class       : LoginRoute
    description : Route to login on system
    version     : 1.0.0
    developer   : Alcindo Schleder <alcindoschleder@gmail.com>
    """

    def dispatch_request(self):
        self.template_name = 'login/logout.html'
        # self.user_context =
        log.info('Request GET at /logout')
        return super(LogoutRoute, self).dispatch_request()


api_functions = RegisterUsersRoute.as_view(APP_BASE_NAME)
server.server_app.add_url_rule(
    '/login/register/<string: pk>',
    view_func=api_functions,
    methods=['GET', 'PUT', 'DELETE']
)
server.server_app.add_url_rule('/login/register', view_func=api_functions, methods=['GET', 'POST'])

api_functions = LoginRoute.as_view(APP_BASE_NAME)
server.server_app.add_url_rule('/login', view_func=api_functions, methods=['GET'])

api_functions = LogoutRoute.as_view(APP_BASE_NAME)
server.server_app.add_url_rule('/logout', view_func=api_functions, methods=['GET'])
