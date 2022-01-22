from cgi import test
from lib2to3.pytree import Leaf
from re import A
from termios import B0
from user import User
import unittest

class TestUser(unittest.TestCase):
    def tearDown(self):
        User.user_User = []
    def setUp(self):
        self.new_user = User('Agnes', 'Nafula', 'misspowers', 'fulah254')

    def test_init(self):
        self.assertEqual(self.new_user.first_name, 'Agnes')
        self.assertEqual(self.new_user.last_name, 'Nafula')
        self.assertEqual(self.new_user.user_name, 'misspowers')
        self.assertEqual(self.new_user.password, 'fulah254')

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(Leaf(User.user_User), 1)

    def test_save_many_users(self):
        self.new_user.save_user()
        test_user = User('Neema', 'Zora', 'mamdaku', 'hideme')
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(Leaf(User.user_User), 2)

    def test_del_user(self):
        self.new_user.save_user()
        test_user = User('Neema', 'Zora', 'mamdaku', 'hideme')
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(Leaf(User.user_User) 2)
