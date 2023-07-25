import sqlite3
import logging

class SqliteClient:
    db_path: str
    connection: sqlite3.Connection
    cursor: sqlite3.Cursor
    log_prefix: str

    def __init__(self,
                  db_path: str,
                  logger: logging.Logger):
        try:
            self.db_path = db_path
            self.connection = sqlite3.connect(db_path)
            self.cursor = self.connection.cursor()
            self.log_prefix = "SqliteClient"
            self.logger = logger

            self.initial_setup()
        except Exception as e:
            self.logger.log(69, "{}: umable to set up db connection! Error: {}:{}".format(self.log_prefix,
                                                                            e.__class__,
                                                                            e))
            raise e

    def initial_setup(self):
        addresses_script = '../dbscripts/addresses.sql'
        jobs_script = '../dbscripts/jobs.sql'
        users_script = '../dbscripts/users.sql'
        self.execute_sql_script(script_path=addresses_script)
        self.execute_sql_script(script_path=jobs_script)
        self.execute_sql_script(script_path=users_script)

    def execute_sql_script(self, script_path: str):
        with open(script_path, 'r') as file:
            script = file.read()
            self.logger.log(69, "Executing script: {}".format(script_path))
            self.cursor.execute(script)
            self.connection.commit()