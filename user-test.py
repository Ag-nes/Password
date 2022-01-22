# from cgi import test
# from lib2to3.pytree import Leaf
# from re import A
# from socket import if_nametoindex
# from termios import B0
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
        self.assertEqual(len(User.user_User), 1)

    def test_save_many_users(self):
        self.new_user.save_user()
        test_user = User('Neema', 'Zora', 'mamdaku', 'hideme')
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_User), 2)

    def test_del_user(self):
        self.new_user.save_user()
        test_user = User('Neema', 'Zora', 'mamdaku', 'hideme')
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_User), 2)

    def test_get_user_by_username(self):
        self.new_user.save_user()
        test_user = User('Neema', 'Zora', 'mamdaku', 'hideme')
        test_user.save_user()
        found_user = User.find_by_user_name('mamdaku')
        self.assertEqual(found_user.user_name, test_user.user_name)

    def test_user_present(self):
        self.new_user.save_user()
        test_user = User('Neema', 'Zora', 'mamdaku', 'hideme')
        test_user.save_user()
        user_present = User.user_present('mamdaku')
        self.assertTrue(user_present)

    def test_show_user(self):
        self.assertEqual(User.show_user(),
                         User.user_User)


if __name__ == '__main__':
 unittest.main()

