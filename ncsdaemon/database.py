from mongokit import Document
import datetime


class Database(object):

    class User(Document):
        __collection__ = 'users'
        __database__ = 'ncsdaemon'
        use_dot_notation = True
        structure = {
            'username': unicode,
            'first_name': unicode,
            'last_name': unicode,
            'email': unicode,
            'institution': unicode,
            'password': unicode,
            'salt': unicode
        }

    class Session(Document):
        __collection__ = 'sessions'
        __database__  = 'ncsdaemon'
        use_dot_notation = True
        structure = {
            'username': unicode,
            'ip': unicode,
            'expires': datetime.datetime
        }

    def __init__(self, conn):
        self.conn = conn
        self.conn.register([User])
