""" This module tests the HTTP API """

import unittest
import json

from ncsdaemon.server import Server

API_PREFIX = '/ncs/api'
URL_PREFIX = API_PREFIX

class APITestCase(unittest.TestCase):
    """ Wrapper class for api test cases """

    def setUp(self):
        server = Server()
        app = server.app;
        app.testing = True
        self.app = app.test_client()
        test_token = 'a_token'
        self.headers = [("token", test_token )]

class TestAuth(APITestCase):
    """ Test the authentication API """

    def test_not_found(self):
        res = self.app.get(URL_PREFIX + 'gibberish')
        self.assertEqual(res.status_code, 404)
        js = json.loads(res.get_data())

    def test_login_empty_request(self):
        res = self.app.post(URL_PREFIX + '/login', data="")
        self.assertEqual(res.status_code, 400)
        js = json.loads(res.get_data())

    def test_login_bad_request(self):
        res = self.app.post(URL_PREFIX + '/login', data="{fjdkslajs}")
        self.assertEqual(res.status_code, 400)
        js = json.loads(res.get_data())

    def test_login_bad_json(self):
        login_info = {"badproperty": "badvalue"}
        res = self.app.post(URL_PREFIX + '/login', data=json.dumps(login_info))
        self.assertEqual(res.status_code, 400)
        js = json.loads(res.get_data())

    def test_login_bad_user(self):
        login_info = {"username": "badusername", "password": "pass"}
        res = self.app.post(URL_PREFIX + '/login', data=json.dumps(login_info))
        self.assertEqual(res.status_code, 401)
        js = json.loads(res.get_data())

    def test_login_bad_pass(self):
        login_info = {"username": "goodusername", "password": "badpass"}
        res = self.app.post(URL_PREFIX + '/login', data=json.dumps(login_info))
        self.assertEqual(res.status_code, 401)
        js = json.loads(res.get_data())

    def test_login_good(self):
        login_info = {"username": "goodusername", "password": "goodpass"}
        res = self.app.post(URL_PREFIX + '/login', data=json.dumps(login_info))
        self.assertEqual(res.status_code, 401)
        js = json.loads(res.get_data())

class TestAuthToken(APITestCase):
    """ Ensure the auth token is required in API requests """

    def test_no_token(self):
        res = self.app.get(URL_PREFIX + '/sim', data='')
        self.assertEqual(res.status_code, 401)

    def test_token(self):
        print self.headers
        res = self.app.get(URL_PREFIX + '/sim', data='',headers=self.headers)
        self.assertEqual(res.status_code, 200)

class TestSim(APITestCase):
    """ Make sure the sim object works as intended """

    def test_get_status(self):
        res = self.app.get(URL_PREFIX + '/sim', data='',headers=self.headers)
        self.assertEqual(res.status_code, 200)
        pass


if __name__ == '__main__':
    unittest.main()
