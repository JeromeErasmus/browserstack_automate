import json
import datetime
from time import mktime
from flask_restful import Resource, Api, abort, reqparse
from flask import request
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy import exc
from automate.server import db

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                print field
                if isinstance(data, datetime.datetime):
                    data = data.isoformat()
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields

        return json.JSONEncoder.default(self, obj)

# Provides basic CRUD operations of resources
class JsonApi(Resource):

	parser = reqparse.RequestParser()
	klass = None
	args = None

	def __init__(self, klass):
		self.klass = klass
		Resource.__init__(self)
		self.add_parse_args(klass)

	def get(self, id):
		result = self.klass.query.get(id)
		if result:
			return self.response(result)
		else:
			abort(404, message="Class {0} doesn't exist".format(id))

	def post(self):
		try:
			obj = self.klass(**self.args)
			db.session.add(obj)
			db.session.commit()
			return self.response(obj)
		except TypeError as e:
			print e
			abort(404, message="One or more values sent in the request object do not match")
		except exc.SQLAlchemyError as e: 
			print e
			abort(404, message="SQLAlchemyError {}".format(e))
		except exc.DBAPIError as e:
			print e
			abort(404, message="DBAPIError {}".format(e))

	def put(self, id):
		abort(404, message="Class {0} doesn't exist".format(id))

	def delete(self, id):
		abort(404, message="Class {0} doesn't exist".format(id))

	def response(self, data):
		return json.loads(json.dumps(data, cls=AlchemyEncoder))

	def add_parse_args(self, obj):
		#if isinstance(obj.__class__, DeclarativeMeta):
		fields = {}
		for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
			self.parser.add_argument(field, type(field))

		self.args = self.parser.parse_args()
