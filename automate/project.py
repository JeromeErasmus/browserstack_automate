import os
import json
import uuid
from time import strftime

class Project():
	def __init__(self):
		self.root_rolder_name = "automate.project"
		self.manifest_file_name = "automate.manifest"
		self.reports_dir_folder_name = "reports"
		self.project_dir = None
		self.manifest_file = None
		self.reports_dir = None
		self.runners = []

	def load(self, project_dir, auto_create_project=False):
		self.project_dir = project_dir
		self.manifest_file = os.path.join(self.project_dir, self.root_rolder_name, self.manifest_file_name)
		self.reports_dir   = os.path.join(self.project_dir, self.root_rolder_name, self.reports_dir_folder_name)

		# check if a project has already been created. If not create one
		if auto_create_project == True:
			self.create_project(project_dir)

		return self.load_manifest()

	def create_project(self, project_dir):
		self.project_dir = project_dir
		self.manifest_file = os.path.join(self.project_dir, self.root_rolder_name, self.manifest_file_name)
		self.reports_dir   = os.path.join(self.project_dir, self.root_rolder_name, self.reports_dir_folder_name)
		targets = [self.manifest_file, self.reports_dir]

		for target in targets:
			if not os.path.exists(os.path.dirname(target)):
			    try:
			        os.makedirs(os.path.dirname(target))
			    except OSError as exc: # Guard against race condition
			        if exc.errno != errno.EEXIST:
			            raise
		
		open(self.manifest_file, 'a').close()


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



	def load_manifest(self):
		try:
			with open(self.manifest_file, "r+") as f:
				contents = f.read()
				if contents:
					self.runners = json.loads(contents)['runners']
				else:
					pass
				f.close()
			print "Loaded manifest file: ", self.manifest_file
			return True
		except IOError:
			print "Error loading manifest file: ", self.manifest_file
			return False

	def save_manifest(self):
		try:
			with open(self.manifest_file, "r+") as f:
				obj = dict(runners=self.runners)
				manifest = json.dumps(obj)
				f.write(manifest)
				f.close()
		except IOError:
			print "Error saving to manifest file:", self.manifest_file
			sys.exit()
