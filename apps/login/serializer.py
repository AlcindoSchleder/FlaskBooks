# -*- coding: utf-8 -*-
from flask_restplus import fields


class UsersSerializer:
    def __call__(self, api):
        return api.model('Users', {
            'pk_categories': fields.Integer(required=False, description='Código da categoria'),
            'dsc_tcat': fields.String(required=True, description='Descrição da categoria'),
            'flag_tcat': fields.Integer(required=True, description='Tipo da categoria'),
            'flag_default': fields.Integer(required=True, description='Marca categoria como default'),
            'date_update': fields.DateTime(description='Data da última atualização do registro'),
            'date_insert': fields.DateTime(description='Data da inserção do registro')
        })
