from __future__ import absolute_import, unicode_literals
import json


class SchemaLoader(object):
    """Schema loader utility implemented as a singleton."""
    _instance = None

    DIRECTORY = 'json_schemas/'

    SCHEMAS = {
        "login_post": DIRECTORY + 'login_post.json',
        "transfer_schema": DIRECTORY + 'transfer_schema.json'
    }

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SchemaLoader, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.schema_dicts = {}
        for schema_name in self.SCHEMAS:
            schema_file = self.SCHEMAS[schema_name]
            with open(schema_file) as f:
                self.schema_dicts[schema_name] = json.loads(f.read())

    def get_schema(self, name):
        return self.schema_dicts[name]
