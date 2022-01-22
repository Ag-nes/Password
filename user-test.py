from user import User
import unittest

class TestUser(unittest.TestCase):
    def tearDown(self):
        User.user_User = []
    def setUp(self):
        self.new_user = User('Agnes', 'Nafula', 'misspowers', 'fulah254')

    def test_init(self):