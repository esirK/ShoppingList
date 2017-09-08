import unittest

from app import app


class TestShoppingListViews(unittest.TestCase):
    def setUp(self):
        """ Create a Test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_app_root_status_code(self):
        result = self.app.get("/")

        # Assert Status code of response
        """ 
        If the user is not logged in He/ She is redirected to Login page
        """
        self.assertEqual(result.status_code, 302)

    def test_status_code_for_login(self):
        """ Test if the Login page is accessible by unauthenticated user"""
        self.assertEqual(200, self.get_result("/login").status_code)

    def test_status_code_for_signup(self):
        """ Test If a non Logged in User can access the signup page"""
        self.assertEqual(200, self.get_result("/signup").status_code)

    def test_un_loggedin_user_can_not_access_the_logout(self):
        """
        Test If a User Will be redirected to the login page on trying
        to access the logout page 
        """
        self.assertEqual(302, self.get_result("/logout").status_code)

    def test_access_to_un_available_endpoint(self):
        self.assertEquals(404, self.get_result("/wtf").status_code)

    def test_anonymous_user_is_always_redirected_to_login(self):
        self.assertEquals(302, self.get_result("/create_shoppinglist").status_code)

    def get_result(self, path):
        """ sends get request to the defined path """
        return self.app.get(path)

if __name__ == '__main__':
    unittest.main()
