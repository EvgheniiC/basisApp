import os

class Config(object): 
    USER = os.environ.get('USER','djoni')
    PASSWORD = os.environ.get('PASSWORD', 'Nehby1984!')
    HOST = os.environ.get('HOST', '127.0.0.1')
    PORT = os.environ.get('PORT','5532')
    DB = os.environ.get('DB','mydb')

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
