# -*- coding: utf-8 -*-
import os
import logging as log
from flask import Flask, Blueprint
from common import COMMON_DIRECTORY, BASE_DIR
from common.helpers.operation_results import OperationResults

CONFIGURE_FILE = f'{COMMON_DIRECTORY}/config.json'
CONFIGURE_DATA = "COMPANY_SECURITY_DATA"
LOG_FORMAT = '[ %(asctime)-15s ] %(message)s'


log.basicConfig(level=log.INFO, format=LOG_FORMAT, filename=f'{BASE_DIR}/log/app.log')


class ICompanyServer(OperationResults):
    """
        Class that initialize API Server, Application Server or both
        * class      ICompanyServer
        * version    1.0.0
        * developer  Alcindo Schleder <alcindoschleder@gmail.com>
    """

    def __init__(self):
        super(ICompanyServer, self).__init__()

        # Create a instance of Flask and get api configuration
        self.server_app = Flask(__name__)

        self.server_prefix = '/server-api'
        self.server_app.config['FLASK_ENV'] = os.environ.get("FLASK_ENV", default="development")
        self.set_environment_config()
        # Create all blueprint apps
        self.server_home_bp = Blueprint('home', __name__)

        # Create a swagger api from home app
        # self.server_api = Api(
        #     app = self.server_home_bp,
        #     version = "1.0",
        #     title = "Vending Machine API 1.0",
        #     description = "Api que acessa recursos da VM",
        #     doc=self.server_prefix + '/docs'
        # )

    def set_environment_config(self):
        from server.config import config_by_name

        mode = config_by_name[self.server_app.config['FLASK_ENV']]

        self.server_app.config['VM_ID'] = config('VM_ID', '')

        # self.server_app.config['SECRET_KEY'] = self.apikey
        self.server_app.config['DEBUG'] = mode.DEBUG
        self.server_app.config['TESTING'] = mode.TESTING
        self.server_app.config['HOST_SERVER'] = mode.HOST_SERVER
        self.server_app.config['SERVER_PORT'] = mode.SERVER_PORT
        self.server_app.config['DB_SERVER'] = mode.DB_SERVER
        self.server_app.config['DATABASE_DRIVER'] = mode.DATABASE_DRIVER
        self.server_app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = mode.PRESERVE_CONTEXT_ON_EXCEPTION
        self.server_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = mode.SQLALCHEMY_TRACK_MODIFICATIONS
    
    def run(self):
        log.info(
            f'Initialising server {self.server_app.config["HOST_SERVER"]}'
            f' on port {self.server_app.config["SERVER_PORT"]}'
        )
        self.server_app.run(
            self.server_app.config['HOST_SERVER'],
            self.server_app.config['SERVER_PORT'],
            debug=self.server_app.config['DEBUG']
        )
