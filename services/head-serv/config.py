class Config(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:<your_password>@192.168.99.100/<your_db_name>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
