import os.path, sys
import json
import uuid
import time
from time import strftime, gmtime
from os import environ

class Project():
	def __init__(self):
		self.app_name = "bs_automate"
		if sys.platform == 'darwin':
			from AppKit import NSSearchPathForDirectoriesInDomains
			self.appdata_path = os.path.join(NSSearchPathForDirectoriesInDomains(14, 1, True)[0], self.app_name, "projects")
		elif sys.platform == 'win32':
			self.appdata_path = os.path.join(environ['APPDATA'], self.app_name, "projects")
		else:
			self.appdata_path = os.path.expanduser(path.join("~", "." + self.app_name, "projects"))

		self.project_folder_name = "automate.project"
		self.manifest_file_name = "automate.prj"
		self.reports_dir_name = "reports"
		self.runners = []
		self.project = dict()

	def load(self, project_dir, auto_create_project=False):
		self.project_dir = project_dir
		self.manifest_file = os.path.join(self.project_dir, self.manifest_file_name)
		self.reports_dir   = os.path.join(self.project_dir, self.project_folder_name, self.reports_dir_name)

		# check if a project has already been created. If not create one
		if auto_create_project == True:
			self.create_project(project_dir)

		return self.load_manifest(self.manifest_file)['runners']

	def get_all_projects(self):
		files = []
		for name in os.listdir(self.appdata_path):
			full_name = os.path.join(self.appdata_path, name)
			if os.path.isdir(full_name):
				manifest_file = os.path.join(full_name, self.manifest_file_name)
				if os.path.exists(manifest_file):
					file_contents = self.load_manifest(manifest_file)
				
					obj = dict(name=file_contents['project']['name'], 
							   modified_date=file_contents['project']['modified_date'],
							   create_date=file_contents['project']['create_date'],
							   manifest_file=file_contents['project']['manifest_file'])
					files.append(obj)
		
		return files


	def create_project(self, name, apiuser=None, apikey=None, tests_location=None):
		self.project['name'] = name
		self.project['apiuser'] = apiuser
		self.project['apikey'] = apikey
		self.project['tests_location'] = tests_location
		self.project['create_date'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		self.project['modified_date'] = self.project['create_date']

		uid = uuid.uuid1().urn
		uid = uid[9:]
		new_project_folder = os.path.join(self.appdata_path, uid)
		manifest_file = os.path.join(new_project_folder, self.manifest_file_name)
		reports_dir = os.path.join(new_project_folder, self.project_folder_name, self.reports_dir_name)
		targets = [manifest_file, reports_dir]

		for target in targets:
			if not os.path.exists(os.path.dirname(target)):
			    try:
			        os.makedirs(os.path.dirname(target))
			    except OSError as exc: # Guard against race condition
			        if exc.errno != errno.EEXIST:
			            raise

		self.project['manifest_file'] = manifest_file
		self.project['project_ref'] = uid

		open(manifest_file, 'a').close()
		self.save_manifest(manifest_file)

		self.project['feature_files'] = self.get_behave_tests_from_dir(tests_location)

		return self.project
		#open(manifest_file, 'a').close()

	def get_behave_tests_from_dir(self, tests_location):
		if not os.path.exists(tests_location):
			return []
		try:
			files = []
			for filex in os.listdir(tests_location):
				if filex.endswith(".feature"):
					files.append(dict(name=filex))
			return files
		except IOError:
			print "Error opening behave tests folder: ", tests_location
			return []

	def add_project_runner(self):
		uid = uuid.uuid1().urn
		uid = uid[9:]
		uid = len(self.runners)+1
		print "LEN", uid
		self.current_runner = self.runners.append(dict(id=uid, reports=[], time_stamp=strftime("%Y-%m-%d %H:%M:%S"))) 
		return uid

	def add_runner_report(self, runner_uid, file_path):
		for runner in self.runners:
			if runner['id'] == runner_uid:
				runner["reports"].append(file_path)
	
	def get_runners(self):
		return self.runners

	def get_runner_by_id(self, runner_id):

		index = None
		for runner in self.runners:
			print runner['id'], runner_id
			if runner['id'] == int(runner_id):
				index = runner
		
		if not index:
			return dict()


		report_obj = dict(time_stamp=index["time_stamp"], id=index["id"], results=[])

		for report in index['reports']:
			try:
				with open(report, "r") as f:
					content = json.loads(f.read())
					report_obj["results"].append(content)
					f.close()
			except IOError:
			    print "Could not read file:", report
			    return False

		return report_obj



	def load_manifest(self, manifest_file):
		try:
			with open(manifest_file, "r+") as f:
				contents = f.read()
				if contents:
					return json.loads(contents)
				else:
					return False
				f.close()
			print "Loaded manifest file: ", manifest_file
		except IOError:
			print "Error loading manifest file: ", manifest_file
			return False

	def save_manifest(self, manifest_file):
		try:
			with open(manifest_file, "r+") as f:
				obj = dict(project=self.project, runners=self.runners)
				data = json.dumps(obj)
				f.write(data)
				f.close()
			return True
		except IOError:
			print "Error saving to manifest file:", manifest_file
			return False
