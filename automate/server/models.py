# automate/server/models.py


import datetime

#from automate.server import app, db, bcrypt
from automate.server import app, db

class Config(db.Model):

    __tablename__ = "config"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    api_user = db.Column(db.String(255), nullable=True)
    access_key = db.Column(db.String(255), nullable=True)
    using_proxy = db.Column(db.Integer, nullable=True)
    proxy = db.Column(db.String(511), nullable=True)

    def __init__(self, api_user, access_key, using_proxy, proxy):
        self.api_user = api_user
        self.access_key = access_key
        self.using_proxy = using_proxy
        self.proxy = proxy

    def get_id(self):
        return self.id

class Project(db.Model):

    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')

        if not kwargs.get('created_on'):
            self.created_on = datetime.datetime.now()
        else:
            self.created_on = kwargs.get('created_on')
            
    def get_id(self):
        return self.id


class Runner(db.Model):

    __tablename__ = "runners"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, project_id):
        self.project_id = project_id
        self.created_on = datetime.datetime.now()

    def get_id(self):
        return self.id

    def get_project_id(self):
        return self.project_id


class Report(db.Model):

    __tablename__ = "reports"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    runner_id = db.Column(db.Integer, nullable=False)
    result = db.Column(db.TEXT, nullable=True)
    created_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, runner_id):
        self.runner_id = runner_id
        self.created_on = datetime.datetime.now()

    def get_id(self):
        return self.id

    def get_runner_id(self):
        return self.runner_id

    def get_result(self):
        return self.result


#class User(db.Model):
#
#    __tablename__ = "users"
#
#    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#    email = db.Column(db.String(255), unique=True, nullable=False)
#    password = db.Column(db.String(255), nullable=False)
#    registered_on = db.Column(db.DateTime, nullable=False)
#    admin = db.Column(db.Boolean, nullable=False, default=False)
#
#    def __init__(self, email, password, admin=False):
#        self.email = email
#        self.password = password
#        #self.password = bcrypt.generate_password_hash(
#        #    password, app.config.get('BCRYPT_LOG_ROUNDS')
#        #)
#        self.registered_on = datetime.datetime.now()
#        self.admin = admin
#
#    def is_authenticated(self):
#        return True
#
#    def is_active(self):
#        return True
#
#    def is_anonymous(self):
#        return False
#
#    def get_id(self):
#        return self.id
#
#    def __repr__(self):
#        return '<User {0}>'.format(self.email)
