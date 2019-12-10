import mysql.connector
import os
import logging


class Database(object):
    def __init__(self, user, password, host):
        self.user = user
        self.password = password
        self.host = host
        self.sql_init_path = '%s/sql_script/init.sql' % os.path.dirname(__file__)

        init_database = mysql.connector.connect(user=self.user, password=self.password, host=self.host)
        my_cursor = init_database.cursor()

        f = open(self.sql_init_path, "r")
        for line in f:
            my_cursor.execute(line)
        f.close()
        init_database.close()
