# automate/server/main/views.py

from flask_restful import Api, abort
from flask import render_template, Blueprint, app
from automate.server.models import Config, Project, Runner, Report
from automate.server.jsonapi import JsonApi
import json
import datetime
from time import mktime

main_blueprint = Blueprint('main', __name__,)


################
#### routes ####
################


@main_blueprint.route('/')
def home():
    return render_template('main/home.html')


@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")


api = Api(main_blueprint)

class ConfigResource(JsonApi):
    def __init__(self):
        JsonApi.__init__(self, Config)


class ProjectListResource(JsonApi):
    def __init__(self):
        JsonApi.__init__(self, Project)


class ProjectResource(JsonApi):
    def __init__(self):
        JsonApi.__init__(self, Project)


class RunnerListResource(JsonApi):
    def __init__(self):
        JsonApi.__init__(self, Runner)

class RunnerResource(JsonApi):
    def __init__(self):
        JsonApi.__init__(self, Runner)

class ReportResource(JsonApi):
    def __init__(self):
        JsonApi.__init__(self, Report)


api.add_resource(ConfigResource, '/config/<int:id>')
api.add_resource(ProjectListResource, '/project')
api.add_resource(ProjectResource, '/project/<int:id>')
api.add_resource(RunnerListResource, '/runner')
api.add_resource(RunnerResource, '/runner/<int:id>')
api.add_resource(ReportResource, '/report/<int:id>')