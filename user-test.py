import unittest


class TestPasswords(unittest.TestCase):
    def tearDown(self):
        Password.user_passwords = []