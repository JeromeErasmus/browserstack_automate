from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import strftime
import requests
import ConfigParser
import json
import subprocess
import os
import clientapp
from project import Project

class Automate():
	def __init__(self):
		self.project = None
		self.load_config()
		self.get_desired_capabilities()

	def run(self, project_dir):
		pass
		self.project = Project()
		self.project.load_project(project_dir, True)
		runner_uid = self.project.add_project_runner()
		
		for tdevice in self.target_devices:
			device_str =  "{0}_{1}_{2}_{3}_{4}".format(tdevice["os"], tdevice["os_version"], tdevice["browser"], tdevice["browser_version"], tdevice["device"])
			result_log_name = "result_"+device_str+"_"+strftime("%Y%m%d%H%M%S")+".log"
			result_log_path = os.path.join(self.project.reports_dir, result_log_name)

		success = self.run_subprocess_behave(self.project.project_dir, result_log_path)

		if success:
			self.project.add_runner_report(runner_uid, result_log_path)

		self.project.save_manifest()
		
		#desired_cap = {'os': 'Windows', 'os_version': 'xp', 'browser': 'IE', 'browser_version': '7.0' }
#
		#driver = webdriver.Remote(
		#    command_executor='http://'+self.API_USER+':'+self.ACCESS_KEY+'@hub.browserstack.com:80/wd/hub',
		#    desired_capabilities=desired_cap)
#
		#driver.get("http://www.google.com")
		#if not "Google" in driver.title:
		#    raise Exception("Unable to load google page!")
		#elem = driver.find_element_by_name("q")
		#elem.send_keys("BrowserStack")
		#elem.submit()
		#print driver.title
		#driver.quit()

	

	def run_subprocess_behave(self, project_dir, result_log_path):
		try:
			p1 = subprocess.Popen('behave ' + project_dir + ' --format json --outfile '+result_log_path)
			return True
		except subprocess.CalledProcessError as e:
			print e.output
			return False

	def get_desired_capabilities(self):
		try:
			f = open("desiredcapabilities.json", "r")
			self.target_devices = json.loads(f.read())
			f.close()
		except IOError:
			print "Error: no desiredcapabilities.json file found"
			return False

	def get_latest_capabilities(self):
		try:
			if self.USING_PROXY == "1":
				proxies={"https":self.PROXY}
			else:
				proxies={}
			r = requests.get("https://www.browserstack.com/screenshots/browsers.json", proxies=proxies)

			if r.status_code == requests.codes.ok:
				try:
					f = open("capabilities.json", "w")
					f.write(r.text)
					f.close()
					return True
				except IOError:
					print "Error: File does not appear to exist."
					return False
			else:
				print "Getting latest capabilities failed. Status code: " + r.status_code
		except requests.exceptions.RequestException as e:   
			print e
			sys.exit(1)


	def load_config(self):
		config = ConfigParser.RawConfigParser()
		config.read('config.ini')

		self.API_USER = config.get('Section_1', 'api_user')
		self.ACCESS_KEY = config.get('Section_1', 'access_key')
		self.USING_PROXY = config.get('Section_1', 'using_proxy')
		self.PROXY = config.get('Section_1', 'proxy')

