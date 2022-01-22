import unittest

from credentials import Credentials


class TestCredentials(unittest.TestCase):
    def tearDown(self):
        Credentials.user_credentials = []
    def setUp(self):
        