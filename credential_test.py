# from cgi import test
import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    def tearDown(self):
        Credentials.user_credentials = []
    def setUp(self):
        self.new_credential = Credentials('instagram', 'powers')

    def test_init(self):
        self.assertEqual(self.new_credential.page, 'instagram')
        self.assertEqual(self.new_credential.credential, 'powers')

    def test_save_page(self):
        self.new_credential.save_page()
        self.assertEqual(len(Credentials.user_credentials), 1)
    
    def test_save_multiple(self):

        self.new_password.save_page()
        test_pass = Credentials('twitter', 'pawa')  
        test_pass.save_page()
        self.assertEqual(len(Credentials.user_credentials), 2)

    def test_delete_page(self):
        self.new_credential.save_page()
        test_pass = Credentials('twitter', 'pawa')
        test_pass.save_page()
        self.new_credential.delete_page()
        self.assertEqual(len(Credentials.user_credentials), 1)

    def test_save_multiple(self):
        self.new_credential.save_page()
        test_pass = Credentials('twitter', 'pawa')
        test_pass.save_page()
        self.assertEqual(len(Credentials.user_credentials), 2)

    def test_delete_page(self):
        self.new_credential.save_page()
        test_pass = Credentials('twitter', 'pawa')
        test_pass.save_page()
        self.new_credential.delete_page()
        self.assertEqual(len(Credentials.user_credentials), 1)

    def test_display_page(self):
        self.assertEqual(Credentials.display_page(), Credentials.user_credentials)

    def test_find_page(self):
        
        self.new_credential.save_page()
        test_pass = Credentials('twitter', 'pawa')  
        test_pass.save_page()
        found_page = Credentials.find_by_page('twitter')
        self.assertEqual(found_page.page, test_pass.page)

    def page_exists(self):
        
        self.new_credential.save_page()
        test_pass = Credentials('twitter', 'pawa')  # new contact
        test_pass.save_page()
        page_exist = Credentials.page_exists('twitter')
        self.assertTrue(page_exist)


if __name__ == '__main__':
    unittest.main()






