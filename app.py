#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from server import server
# Need to import all resources
from workspaces.home.view import HomeRoute

# Register all Blueprint
server.server_app.register_blueprint(server.server_home_bp)

# run dev, prod or test
if __name__ == '__main__':
    server.run()
