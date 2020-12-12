# -*- coding: utf-8 -*-
from common import COMMON_DIRECTORY
from common.helpers.load_config import LoadJsonFiles
from common.helpers.exceptions import HttpCodeNotFound


class ErrorCodes:
    """
        class       : httpErrorCodes
        description : Exception when HTTPD code on result is invalid
        version     : 1.0.0
        developer   : Alcindo Schleder
    """
    ERROR_FILENAME = f'{COMMON_DIRECTORY}/httpErrorCodes.json'
    
    def __init__(self):
        conf = LoadJsonFiles(self.ERROR_FILENAME) 
        self._error_codes_list = dict(conf.dict_data)

    @property
    def error_list(self):
        return self._error_codes_list

    @property
    def error_group(self, code: int = 200) -> str:
        grp = self._isvalid(code)
        if grp:
            return self._error_codes_list[grp]["code"]
        else:
            raise NotImplementedError(404)
    
    @property
    def error_group_and_code_descr(self, code: int = 200) -> dict:
        grp = self._isvalid(code)
        if grp:
            return { 
                "groupName": self._error_codes_list[grp]["name"],
                "codeDescr": self._error_codes_list[grp]["code"][code]
            }
        else:
            raise NotImplementedError(404)

    def _isvalid(self, code: int = 200):
        grp = str(code)
        str_code = grp
        if code < 99:
            grp = '4'
        grp = grp[0] + 'xx'
        if self._error_codes_list.get(grp, None) is not None and \
                self._error_codes_list[grp].get("code", None) is not None and \
                self._error_codes_list[grp]["code"].get(
                    str_code,
                    None
                ) is not None:
            return grp, str_code
        else:
            return False, False
    
    def error_code_descr(self, code: int = 200) -> str:
        grp, str_code = self._isvalid(code)
        if grp:
            return self._error_codes_list[grp]["code"][str_code]
        else:
            raise HttpCodeNotFound(f'{grp}:{str_code}')
    
    def inspect_dict_data(self, data: dict, descr: str, level: int = 1):
        key = None
        value = None
        for key, value in data.items():
            if value == descr:
                return key, value
            if type(value) == dict:
                level += 1
                key, value = self.inspect_dict_data(value, descr, level)
                level -= 1
                if value == descr:
                    break
        return key, value

    def get_error_code_from_descr(self, description: str) -> str:
        result = self.inspect_dict_data(self._error_codes_list, description)
        return result[1]
