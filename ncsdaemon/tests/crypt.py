""" This module tests the  simulator integration """

import unittest
import ncsdaemon.crypt as crypt


class CryptTestCase(unittest.TestCase):
    """ Test case used for cryptography """

    def test_salt(self):
        salt = crypt.Crypt.generate_salt()
        self.assertTrue(isinstance(salt, str))
        self.assertEqual(len(salt), 64)

    def test_token(self):
        token = crypt.Crypt.generate_user_token()
        self.assertTrue(isinstance(token, str))
        self.assertEqual(len(token), 64)

    def test_password_hashing(self):
        password = crypt.Crypt.hash_password("password", "123456")
        self.assertTrue(isinstance(password, str))
        self.assertEqual(len(password), 64)

    def test_sim_id(self):
        sim_id = crypt.Crypt.generate_sim_id()
        self.assertTrue(isinstance(sim_id, str))
        self.assertEqual(len(sim_id), 64)

class CryptDummyTestCase(unittest.TestCase):
    """ Test case used for cryptography """

    def test_salt(self):
        salt = crypt.CryptDummy.generate_salt()
        self.assertEqual(salt, "abc123")

    def test_token(self):
        token = crypt.CryptDummy.generate_user_token()
        self.assertEqual(token, "a_token")

    def test_password_hashing(self):
        password = crypt.CryptDummy.hash_password("password", "123456")
        self.assertEqual(password, "password")

    def test_sim_id(self):
        sim_id = crypt.CryptDummy.generate_sim_id()
        self.assertEqual(sim_id, "123")

if __name__ == "__main__":
    unittest.main()
