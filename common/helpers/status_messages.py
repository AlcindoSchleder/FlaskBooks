# -*- coding: utf-8 -*-
from enum import Enum


class MessageType(Enum):
    none = 0
    successfully = 1
    message = 2
    warning = 4
    error = 8


class Messages:
    """
        Classe que implementa uma mensagem em uma lista para posterior consulta
        * class      Messages
        * requires   python 3.7
        * version    1.0.0
        * developer  Alcindo Schleder <alcindo.schleder@amcom.com.br>
    """
    _msg_type = None
    _msg_code = None
    _message = None
    _list_msg = []

    def __init__(self, **kwargs):
        """
        Constructor
        @param kwargs dict: Dicionário de dados com os parâmetros da mensagem
                        msg: str: Mensagem a ser exibida
                        code: int: Código HTTP da mensagem
                        type: int: Typo da mensagem (Messages.types)
        """
        msg = kwargs.get('msg', None)
        if msg is None:
            msg = "Operation realized Successfully!"
        else:
            kwargs.pop('msg')
        code = kwargs.get('code', None)
        if code is None:
            code = 200
        else:
            kwargs.pop('code')
        self._msg_type = kwargs.get('msg_type', MessageType(0))
        self._msg_code = code
        self._message = msg
        self._list_msg = None

    def append(self, obj):
        if self._list_msg is None:
            self._list_msg = []
        self._list_msg.append(obj)

    @property
    def has_errors(self):
        if self._list_msg is None:
            for idx in self._list_msg:
                if self._list_msg.message_type > 0:
                    return False
            return (self._list_msg is not None) and (len(self._list_msg) > 0)


    @property
    def list_msg(self):
        return self._list_msg
