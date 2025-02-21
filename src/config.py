class Config():
    pass

class Development(Config):
    MYSQL_DATABASE_USER = "root"
    MYSQL_DATABASE_PASSWORD ="root"
    MYSQL_DATABASE_DB="contacts"
    pass

class Build(Config):
    pass