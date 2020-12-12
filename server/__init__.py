# -*- coding: utf-8 -*-
from server.company_server import ICompanyServer, log
"""
    INITIALIZE SERVER
"""
log.info('Initializing Application...')
server = ICompanyServer()
server_app = server.server_app
