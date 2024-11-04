# database context manager

from pymysql import connect
from pymysql.err import OperationalError

class DBContextManager:

    # метод инициализации
    def __init__(self, db_config: dict):
        self.conn = None
        self.cursor = None
        self.config = db_config

    #     специфические операции (подключение, придать объектам значения)
    def __enter__(self):
        try:
            self.conn = connect(**self.config)
            self.cursor = self.conn.cursor()
            return self.cursor

        except OperationalError as err:
            print(err.args)
            return None

    #     параметры - ошибки, которые могли появиться на этапе выполнения курсора, то sql-сервер передаст в метод enter
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(exc_type)
        if self.cursor:
            if exc_type:
                self.conn.rollback()
            else:
                self.conn.commit()
            self.cursor.close()
            self.conn.close()

        return True