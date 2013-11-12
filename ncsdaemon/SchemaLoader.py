""" Loads JSON schema objects for validation """
import json

class SchemaLoader(object):
    """ Schema Loader Singleton """
    _instance = None

    DIRECTORY = '../json_schemas/'

    SCHEMAS = {
        "login_post": DIRECTORY + 'login_post.json'
    }

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SchemaLoader, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        for schema_name, schema_file in self.SCHEMAS:
            with open(schema_file) as f:
                self[schema_name] = json.loads(f.read())
