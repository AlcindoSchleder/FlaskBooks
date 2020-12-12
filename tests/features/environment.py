# -*- coding: utf-8 -*-
"""
    Unit        : tests.environment
    Description : Define environment configuration to execute the tests
    developer   : Alcindo Schleder
    version     : 1.0.0
"""
import os
import ipdb
from common import COMMON_DIRECTORY, BASE_DIR
from server import server_app
from apps.login.view import HomeRoute


def before_feature(context, feature):
    context.root_path = os.path.dirname(os.path.dirname(BASE_DIR))
    context.flask = server_app
    context.flask.testing = True
    context.flask_context = context.flask.test_request_context()
    context.flask_context.push()
    context.client = context.flask.test_client()


def after_feature(context, feature):


def after_step(context, step):
    if step.status == 'failed':
        ipdb.spost_mortem(step.exc_traceback)
