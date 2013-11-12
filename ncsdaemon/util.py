""" Loads JSON schema objects for validation """
import json
from flask import jsonify

class ServerUtils(object):
    """ Miscellaneous server utilities """

    @classmethod
    def json_and_status(cls, json, status):
        res = jsonify(json)
        res.status_code = status
        return res

    @classmethod
    def json_message(cls, message):
        return {"message": message}

class SchemaLoader(object):
    """ Schema Loader Singleton """
    _instance = None

    DIRECTORY = 'json_schemas/'

    SCHEMAS = {
        "login_post": DIRECTORY + 'login_post.json'
    }

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SchemaLoader, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.schema_dicts = {}
        for schema_name in self.SCHEMAS:
            schema_file = self.SCHEMAS[schema_name]
            with open(schema_file) as f:
                self.schema_dicts[schema_name] = json.loads(f.read())

    def get_schema(self, name):
        return self.schema_dicts[name]
