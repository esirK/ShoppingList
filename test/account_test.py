import unittest

from app.Exceptions import UserAlreadyExist, UserDoesNotExist
from app.models.accounts import Accounts
from app.models.user import User


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Accounts()
        self.user = User("Master", "master@gmail.com", "199410")

    def test_create_user(self):
        """
        test if a user is created by the create_user method
        :return: 
        """
        self.account.add_user(self.user)
        self.assertEqual(1, len(self.account.all_users()))

    def test_exception_raised_on_creating_already_existing_user(self):
        self.account.add_user(self.user)
        with self.assertRaises(UserAlreadyExist):
            self.account.add_user(self.user)

    def test_rm_user(self):
        self.account.add_user(self.user)
        self.assertEqual(1, len(self.account.all_users()))
        self.account.rm_user("master@gmail.com")
        self.assertEqual(0, len(self.account.all_users()))

    def test_removing_a_non_user_raises_exception(self):
        with self.assertRaises(UserDoesNotExist):
            self.account.rm_user("wobbywobby@gmail.com")

    def test_can_add_many_user(self):
        for x in range(10):
            user = User("EsirTT", "kimkings@gmail.com" + str(x), "199410")
            self.account.add_user(user)
        self.assertEqual(10, len(self.account.all_users()))


if __name__ == '__main__':
    unittest.main()
