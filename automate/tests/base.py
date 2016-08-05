# automate/server/tests/base.py


from flask_testing import TestCase
from project.server import app, db
from project.server.models import Config, Project, Runner, Report #User
from project.server import app, db
import random, string


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('project.server.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()

        config = Config(api_user="1", access_key="1", using_proxy="1", proxy="1")
        db.session.add(config)
        db.session.commit()

        project_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        project = Project(name=project_name)
        db.session.add(project)
        db.session.commit()
        
        runner = Runner(project_id=project.get_id())
        db.session.add(runner)
        db.session.commit()
        
        report = Report(runner_id=runner.get_id())
        db.session.add(report)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
