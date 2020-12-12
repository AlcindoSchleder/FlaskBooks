# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, text, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists
from common.base.db.interfaceDB import IDatabases, READ_PERM
from common.base.db.configure_connection import ConfigureConnection


class Connection(IDatabases):
    """
        class       : Connection
        Description : Class that implements a Basic DataBase Connection
        version     : 1.0.0
        Developer   : Alcindo Schleder
        package     : i-City Identification Plataform
    """
    _app = None
    _app_config = None
    _engine = None

    def __init__(self, app):
        super(Connection, self).__init__()
        self._app = app
        self._set_driver(self._app.config['DATABASE_DRIVER'])

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self._engine.closed:
            self._engine.dispose()

    def _set_driver(self, driver: str):
        """
        Change database driver and configure DSN
        """
        self._app_config = ConfigureConnection()
        self._app.config['ICITY_SECURITY_DATA'] = self._app_config.global_config['ICITY_SECURITY_DATA']
        try:
            if self._app_config.result['state']['sttCode'] == 200:
                self._app_config.db_driver = driver
                self._DATABASE_URI = self._app_config.connection_uri()
                self._config_db()
        except Exception as e:
            msg = f'A internal unexpected error occurred: ({e.args})'
            self.status_code = 500
            self.status_message = msg
            raise Exception(msg)

    def _config_db(self):
        """
        Configure DSN to preparing for new conection
        """
        self.status_code = 200
        msg = f'Database {self._app_config.database_name} on ' \
              f'{self._app_config.database_driver} '
        msg += f'({self._DATABASE_URI}) not found. ' \
               f'Please verify with your sysdba!'
        try:
            if not database_exists(self._DATABASE_URI):
                self.status_code = 404
                self.status_message = msg
        except Exception as e:
            self.status_code = 500
            self.status_message = f'{msg}: ({e.args})'
            raise Exception(f'{msg}: ({e.args})')
        
    def _create_session(self):
        """
        Create a connection session with the database
        """
        try:
            if self._engine is None:
                msg = 'Engine not created ou closed!'                
                self.status_code = 301
                self.status_message = 'Database not connected!'
                raise Exception(msg)
            db_session = sessionmaker(bind=self._engine)
            db_session.configure(bind=self._engine)
            self._session = db_session(autocommit=True)
        except Exception as e:
            if self._session and self._session.is_active:
                self._session.close()
            msg = 'Can`t create a session into Database ' \
                  f'{self._db_table.name}: ({e.args})'
            self.status_code = 500
            self.status_message = msg
            raise Exception(msg)

    def connect(self):
        """
        Do database connection
        """
        self.status_code = 200
        if not self.is_connected:
            self._app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            self._app.config['SQLALCHEMY_DATABASE_URI'] = self._DATABASE_URI
            try:
                self._engine = create_engine(self._DATABASE_URI, echo=False)
                self._create_session()
            except Exception as e:
                if self._engine:
                    self._engine.dispose()
                msg = 'A Unexpected error occurred on connect database, ' \
                      f'please contact network admin! ({e.args})'
                self.status_code = 500
                self.status_message = msg
                raise Exception(msg)

    def disconnect(self):
        """
        Database disconnect
        """
        if self._session is not None and self._session.is_active:
            self._session.close()

    def _can_exec(self, permission):
        super(Connection, self)._can_exec(permission)

    def exec_command(self, query: str, params: dict = None):
        """
        Execute a query specific on database and store result into self.db_data
        """
        self.status_code = 200
        if not self._session.is_active:
            self._session.begin()
        try:
            result = self._session.query(self.db_table).from_statement(text(query)).params(params).all()
            self._session.commit()
            self.data = result
        except Exception as e:
            self._session.rollback()
            self.status_code = 500
            self.status_message = f'Erro on execute sql command! {e.args}'
        finally:
            self._session.close()

    def browse_record(self, filters=None, order_by=None, start: int = 0, limit: int = 0):
        """
        Exceute a database query on database and store results in self.data
        """
        page = {}
        self.status_code = 200
        try:
            if not self._session.is_active:
                self._session.begin()

            if start > 0 and limit > 0:
                page = {
                    'summary': {
                        'count': self._session.query(func.count(self._db_table)),
                        'start': start,
                        'limit': limit,
                        'next': '/',
                        'prev': '/'
                    },
                    'records': []
                }
            if filters is None:
                if start > 0 and limit > 0:
                    rows = self._session.query(self._db_table).limit(limit).offset(start * limit)
                else:
                    rows = self._session.query(self._db_table).all().order_by(order_by)
                for row in rows:
                    page['records'].append(row.as_dict())
            else:
                for row in self._session.query(self._db_table).filter(filters).all():
                    page['records'].append(row.as_dict())
            self.data = page

            self._session.commit()
        except Exception as e:
            self._session.rollback()
            self.status_code = 500
            self.status_message = f'Erro ao pesquisar registros na tabela {self.db_table_name}! : {e.args}'
        finally:
            self._session.close()

    def insert_record(self):
        """
        Execute a insert query into database and store result in data property
        """
        self.status_code = 200
        try:
            if not self._session.is_active:
                self._session.begin()
            data = self._session.add(self._db_table)
            self.data = data
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            self.status_code = 500
            self.status_message = 'Erro ao inserir um registro na tabela' \
                                  f' {self.db_table_name}! :{e.args}'
        finally:
            self._session.close()

    def update_record(self):
        """
        Execute a update query into database and store result into data property
        """
        self.status_code = 200
        try:
            if not self._session.is_active:
                self._session.begin()
            data = self._session.update(self._db_table)
            self.data = data
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            self.status_code = 500
            self.status_message = 'Erro ao editar um registro na tabela' \
                                  f' {self.db_table_name}! :{e.args}'
        finally:
            self._session.close()

    def delete_record(self):
        """
        Execute a delete query into database and store result into data property
        """
        self.status_code = 200
        try:
            if not self._session.is_active:
                self._session.begin()
            self._session.delete(self._db_table)
            self.data = {}
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            self.status_code = 500
            self.status_message = 'Erro ao deletar um registro na tabela ' \
                                  f'{self.db_table_name}! :{e.args}'
        finally:
            self._session.close()

    def set_permission(self, new_permission: int = READ_PERM):
        super(Connection, self).set_permission(new_permission)
