# -*- coding: utf-8 -*-
from flask_restplus import reqparse

PageArgs = reqparse.RequestParser()
PageArgs.add_argument('start', type=int, required=False)
PageArgs.add_argument('limit', type=int, required=False,
                      choices=[10, 20, 30, 40, 50], default=20)


class InterfaceModel:
    """
        class       : InterfaceModel (Interface)
        description : Class that Define a serializer model
        version     : 1.0.0
        developer   : Alcindo Schleder
    """

    LIST_RECORD_STRUCT = {
        'summary': {
            'count': 0,
            'start': 0,
            'limit': 0,
            'next': '/',
            'prev': '/'
        },
        'records': []
    }

    def calc_list_summary(self, url: str, start: int, limit: int, count: int) -> dict:
        """
        Return pagination of records
        """
        if count > start and limit > 0:
            # make response
            self.LIST_RECORD_STRUCT['summary']['start'] = start
            self.LIST_RECORD_STRUCT['summary']['limit'] = limit
            self.LIST_RECORD_STRUCT['summary']['count'] = count
            # make URLs
            # make previous url
            if start == 1:
                self.LIST_RECORD_STRUCT['summary']['prev'] = ''
            else:
                start_copy = max(1, start - limit)
                limit_copy = start - 1
                self.LIST_RECORD_STRUCT['summary']['prev'] = \
                    f'{url}?start={start_copy}&limit={limit_copy}'
            # make next url
            if start + limit > count:
                self.LIST_RECORD_STRUCT['summary']['next'] = ''
            else:
                start_copy = start + limit
                self.LIST_RECORD_STRUCT['summary']['next'] = \
                    f'{url}?start={start_copy}&limit={limit}'
        return self.LIST_RECORD_STRUCT
