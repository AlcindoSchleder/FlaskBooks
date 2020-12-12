# -*- coding: utf-8 -*-
from common.helpers.load_config import LoadJsonFiles
from common.helpers.operation_results import OperationResults
from server.company_server import CONFIGURE_FILE, CONFIGURE_HASH

SUPPORTED_DRIVERS = ['mysql', 'mongodb', 'sqlite', 'postgresql']
DRIVER_MAP = {
    "mysql": "MYSQL_DATABASE_CONNECTION",
    "postgresql": "PGSQL_DATABASE_CONNECTION",
    "sqlite": "SQLITE_DATABASE_CONNECTION",
    "infuxdb": "INFLUX_DATABASE_CONNECTION",
    "mongodb": "MONGO_DATABASE_CONNECTION"
}


class ConfigureConnection(OperationResults):
    """
        class       : ConfigureConnection
        Description : Class that to do the database configuration
        version     : 1.0.0
        Developer   : Alcindo Schleder
        package     : i-City Identification Plataform
    """

    def __init__(self):
        super(ConfigureConnection, self).__init__()
        self.status_code = 200
        self._global_config = None
        self._db_driver = 'sqlite'
        self._config_driver = DRIVER_MAP[self._db_driver]
        try:
            ljf = LoadJsonFiles(CONFIGURE_FILE)
            self.result = ljf.check_file_hash(CONFIGURE_HASH)
            if self.status_code != 200:
                raise Exception(self.status_message)
            self._global_config = ljf.dict_data
        except Exception as e:
            msg = f'Can not load config file {CONFIGURE_FILE}!!\nRazon: {e.args}'
            self.status_code = 500
            self.status_message = msg
            raise Exception(msg)

    def connection_uri(self):
        if self.status_code != 200:
            return False

        driver = self._global_config[self._config_driver]["database"]["driver"]
        host = self._global_config[self._config_driver]["database"]["host"]
        user = self._global_config[self._config_driver]["database"]["user"]
        db_name = self._global_config[self._config_driver]["database"]["db_name"]
        pwd = self._global_config[self._config_driver]["database"]["password"]
        if driver == 'sqlite':
            from data import DATABASE_PATH
            return f'{driver}:///{DATABASE_PATH}/{db_name}'
        else:
            return f'{driver}://{user}:{pwd}@{host}/{db_name}'

    @property
    def global_config(self):
        return self._global_config

    @property
    def database_driver(self):
        return self._global_config[self._config_driver]["database"]["driver"]

    @property
    def database_name(self):
        return self._global_config[self._config_driver]["database"]["db_name"]

    @property
    def database_user(self):
        return self._global_config[self._config_driver]["database"]["user"]

    @property
    def database_password(self):
        return self._global_config[self._config_driver]["database"]["password"]

    @property
    def db_driver(self):
        return self._db_driver

    @db_driver.setter
    def db_driver(self, driver: str):
        if driver in SUPPORTED_DRIVERS:
            self._db_driver = driver
            self._config_driver = DRIVER_MAP[self._db_driver]
        else:
            self.status_message = f'Driver {self._db_driver} not implemented yet!'
