from dotenv import load_dotenv
import os

load_dotenv()

class Config():
    pass

class Development(Config):
    MYSQL_DATABASE_USER = "root"
    MYSQL_DATABASE_PASSWORD ="root"
    MYSQL_DATABASE_DB="contacts"
    pass

class Build(Config):
    print('User: {}\nPassword: {}\nHost: {}\nDB: {}\n'.format(os.getenv("MYSQL_DATABASE_USER"),os.getenv("MYSQL_DATABASE_PASSWORD"),os.getenv("MYSQL_DATABASE_HOST"),os.getenv("MYSQL_DATABASE_DB")))
    MYSQL_DATABASE_USER = os.getenv("MYSQL_DATABASE_USER")
    MYSQL_DATABASE_PASSWORD = os.getenv("MYSQL_DATABASE_PASSWORD")
    MYSQL_DATABASE_HOST = os.getenv("MYSQL_DATABASE_HOST")
    MYSQL_DATABASE_PORT = int(os.getenv("MYSQL_DATABASE_PORT"))
    MYSQL_DATABASE_DB = os.getenv("MYSQL_DATABASE_DB")
    pass