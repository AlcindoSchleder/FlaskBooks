#!/usr/bin/env python
# -*- coding: utf-8 -*-
from server import server_app as app
from common import BASE_DIR
from common.base.db.connection import Connection



def create_stored_procedure() -> str:
    result = 'Create Stored Procedure Sucefully!'
    fn = f'{BASE_DIR}/data/databse.sql'
    try:
        f = open(fn, 'r')
        with connection.cursor() as cursor:
            cursor.execute(f.read())
    except Exception as e:
        result = f'Erro ao rodar o script no banco de dados!\n  ==> {e}'
    return result
