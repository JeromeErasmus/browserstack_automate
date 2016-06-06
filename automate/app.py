#from project import Project
#from automate import Automate
import sys
from ConfigParser import SafeConfigParser
import argparse
from automate import Automate
import clientapp

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Process some integers.')
	
	parser.add_argument('operations', metavar='N', type=str, nargs='+', 
		help='Instructs the application what operations to perform. \nThe following operations can be called: run \n client \n getallcapabilities\n')
	parser.add_argument('-c', '--capabilities', type=int, help='Get latest capabilities', required=False)
	parser.add_argument('-path', '--path', type=str, help='Folder path to Behave project files', required=False, nargs='+')

	args = parser.parse_args()
	automateapp = Automate()

	for operation in args.operations:
		if operation == 'getallcapabilities':
			automateapp.get_latest_capabilities()
		elif operation == 'client':
			clientapp.run()
		elif operation == 'run':
			if not args.path:
				print "Error: no project path specified"
				sys.exit(1)
			else:
				automateapp.run(args.path[0])

