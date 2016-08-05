# manage.py

from subprocess import Popen, PIPE, CalledProcessError
import platform
import os
import unittest


from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from automate.server import app, db
from automate.server.models import Project, Config


migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('automate/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()

@manager.command
def create_data():
    """Creates sample data."""
    pass

@manager.command
def install():
    """ Install the app """
    
    create_db()
    create_data()


if __name__ == '__main__':
    manager.run()
