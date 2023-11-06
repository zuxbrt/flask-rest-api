import os
from dotenv import load_dotenv
import pymysql.cursors

load_dotenv()

connection = pymysql.connect(host=os.getenv("MYSQL_DATABASE_HOST"),
                             user=os.getenv("MYSQL_DATABASE_USER"),
                             password=os.getenv("MYSQL_DATABASE_PASSWORD"),
                             database=os.getenv("MYSQL_DATABASE_DB"),
                             charset=os.getenv("MYSQL_DATABASE_CHARSET"),
                             cursorclass=pymysql.cursors.DictCursor)

def setup():
    with connection:
        # with connection.cursor() as cursor:
        #     # new record
        #     sql = "INSERT INTO `users` (`email`, `password`) values (%s, %s)"
        #     cursor.execute(sql, ('admin@flaskapi.com', 'test1234'))

        # # commit to save
        # connection.commit()

        with connection.cursor() as cursor:
            # read record
            sql = "SELECT `id`, `email` FROM users where `email`=%s"
            cursor.execute(sql, ('admin@flaskapi.com'))
            result = cursor.fetchone()
            return result