import os

db_dir = "database/db.sqlite"


class Config(object):
    Debug = True
    Testing = True
    BOOTSTRAP_BOOTSWATCH_THEME = 'Simplex'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(db_dir)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SECURE = True


class DevelopmentConfig(Config):
    Debug = True
    BOOTSTRAP_BOOTSWATCH_THEME = 'Simplex'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(db_dir)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SECURE = True
    

