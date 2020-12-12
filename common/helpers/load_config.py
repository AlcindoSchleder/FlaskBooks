# -*- coding: utf-8 -*-
import json
import os  
import hashlib
from common.helpers import default_object


class LoadJsonFiles:
    """
        class       : LoadJsonFiles
        descritption: Class that load a json file and transform in a dict to return
        author      : Alcindo Schleder
        version     : 1.0.0
        package     : i-City Identification Plataform
    """
    BLOCKSIZE = 65536

    def __init__(self, filename: str, data_config: str = None):
        self._fn = filename
        self._dataConfig = data_config
        if not self._check_file():
            self._fn = None
            raise Exception(f'File {filename} not found!')

        self._json_file_config = {}
        try:
            if self._fn:
                with open(self._fn, 'r') as f:
                    self._json_file_config = json.load(f)
                    f.close()
        except Exception as e:
            self._jsonFileConfig = {}
            raise Exception(e.args)

    def _check_file(self):
        return os.path.isfile(self._fn)

    def _generate_hash(self):
        msg_hash = hashlib.sha256()
        with open(self._fn, 'rb') as afile:
            buf = afile.read(self.BLOCKSIZE)
            while len(buf) > 0:
                msg_hash.update(buf)
                buf = afile.read(self.BLOCKSIZE)
        return msg_hash

    def check_file_hash(self, config_filehash: str):
        res = default_object
        if not self._check_file():
            res['state']['sttCode'] = 401
            res['state']['sttMsgs'] = 'Erro: Arquivo de configuração não existe!'
            return res
        msg_hash = self._generate_hash()
        if config_filehash != msg_hash.hexdigest():
            res['state']['sttCode'] = 401
            res['state']['sttMsgs'] = 'Erro: Arquivo de configuração foi comprometido!'
        return res

    @property
    def dict_data(self):
        if self._dataConfig:
            return dict(self._json_file_config[self._dataConfig])
        else:
            return dict(self._json_file_config)
