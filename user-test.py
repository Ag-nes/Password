from user import User
import unittest

class TestUser(unittest.TestCase):
    def tearDown(self):
        User.user_User = []
    def setUp(self):