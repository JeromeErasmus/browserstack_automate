from flask import Flask, Response, jsonify, render_template, request, redirect, url_for
from project import Project
import time
import os.path as path
import json
from json import JSONEncoder

client_app = Flask(__name__)
client_app.debug = True
project = Project()
#project.load("samples/")

def run():
	client_app.run("localhost", 5050)
	
	

#def event_stream():
#	last_modified = path.getmtime(project.manifest_file)
#	while True:
#		file_now =  path.getmtime(project.manifest_file)
#
#		if file_now != last_modified:
#			#print "Detected change in manifest file. Pushing changes to client"
#			last_modified = file_now
#			yield "data: "+json.dumps(project.get_runner_latest_report())+"\n\n"
#			#print project.get_runner_latest_report()
#		time.sleep(2)

class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class CustomResponse():
	def __init__(self, status, data=None, message=None):
		self.data = data
		self.status = status
		self.message = message

@client_app.route('/')
def index():
	return render_template('index.html')


@client_app.route('/data/runners')
def data_runners():
	print jsonify(dict(data=project.get_runners()))
	return jsonify(dict(data=project.get_runners()))

@client_app.route('/data/results/<result_id>',methods=["GET"])
def data_result_by_id(result_id):
	return jsonify(project.get_runner_latest_report())
	return jsonify(project.get_runner_by_id(result_id))

@client_app.route('/project', methods=["GET", "POST"])
def projectdata():
	if request.method == 'POST':
		if request.get_data():
			data = json.loads(request.get_data())
			project_data = project.create_project(data['name'], data['apiuser'], data['apikey'], data['tests_location'])
			resp = CustomResponse("success", project_data, '')
		else:
			resp = CustomResponse("error", None, "Incorrect post data")	
		return MyEncoder().encode(resp)

	elif request.method == 'GET':
		if request.args.get('project_path'):
			data = project.load(request.args.get('project_path'))
			if data:
				resp = CustomResponse("success", data, '')
			else:
				resp = CustomResponse("error", None, 'No projects found')

		else:
			data = project.get_all_projects()
			if data:
				resp = CustomResponse("success", data, '')
			else:
				resp = CustomResponse("error", None, 'No project found')
			
			
		
		return MyEncoder().encode(resp)
		
	return jsonify([])

#@client_app.route('/stream')
#def stream():
#	return Response(event_stream(), mimetype="text/event-stream")