import pymysql
import config

def get_connection():
    try:
        connection = pymysql.connect(
            host=config.MYSQL_HOST,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            database=config.MYSQL_DATABASE,
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("Database connected successfully!")
        return connection
    except Exception as e:
        print("Database connection failed:")
        print(e)