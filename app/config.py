import os


class Config(object):
    APPNAME = "app"
    ROOT = os.path.abspath(APPNAME)
    UPLOAD_PATH = '/static/upload'
    SERVER_PATH = ROOT + UPLOAD_PATH

    USER = os.environ.get('USER', 'djoni')
    PASSWORD = os.environ.get('PASSWORD', 'Nehby1984!')
    # HOST = os.environ.get('HOST', '127.0.0.1')
    # PORT = os.environ.get('PORT', '5532')
    HOST = os.environ.get('HOST', 'postgres')
    PORT = os.environ.get('PORT', '5432')
    DB = os.environ.get('DB', 'mydb')

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
