# -*- coding: utf-8 -*-
from common.helpers.error_codes import ErrorCodes
from common.helpers import default_object


class OperationResults(ErrorCodes):
    """
        class       : OperationResults
        descritption: Class to normalize messages to app
        author      : Alcindo Schleder
        version     : 1.0.0
        package     : i-City Identification Plataform
    """

    def __init__(self, *args, **kwargs):
        super(OperationResults, self).__init__()
        self._result = default_object

    @staticmethod
    def _validate_dictionary(value: dict = None):
        return bool((value.get("data")) and (value.get("state")) and
                    (value["state"].get("sttCode")) and
                    (value["state"].get("sttMsgs")))

    def get_result(self):
        return self._result

    def set_result(self, value: dict = None):
        if value and self._validate_dictionary(value):
            self._result = value
        else:
            self._result = default_object

    @property
    def status_code(self):
        return self._result['state']['sttCode']

    @status_code.setter
    def status_code(self, stt_code: int):
        self._result['state']['sttCode'] = stt_code
        self._result['state']['sttMsgs'] = self.error_code_descr(stt_code)

    @property
    def data(self):
        return self._result["data"]

    @data.setter
    def data(self, value):
        self._result["data"] = value

    @property
    def status_message(self):
        return self._result["state"]["sttMsgs"]

    @status_message.setter
    def status_message(self, message: str):
        self._result['state']['sttMsgs'] = message
        if self._result['state']['sttCode'] == 200:
            self._result['state']['sttCode'] = self.get_error_code_from_descr(message)
