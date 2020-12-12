# -*- coding: utf-8 -*-
from flask_restplus import fields


class UsersSerializer:
    """
    class       : UsersSerializer
    description : Serializer Users Data
    version     : 1.0.0
    developer   : Alcindo Schleder <alcindoschleder@gmail.com>
    """
    def __call__(self, api):
        return api.model('Users', {
            'pk_user': fields.Integer(required=False, description='Código'),
            'email': fields.String(required=True, description='e-mail'),
            'username': fields.String(required=True, description='Nome'),
            'login': fields.String(required=True, description='Login'),
            'passwd': fields.String(required=True, description='Senha'),
            'date_update': fields.DateTime(description='Última atualização'),
            'date_insert': fields.DateTime(description='Data de Inserção')
        })
