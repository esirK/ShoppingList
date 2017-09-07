import unittest

from app.Exceptions import ShoppingListDoesNotExist, ShoppingListAlreadyExist
from app.models.ShoppingList import ShoppingList
from app.models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """Create global User And ShoppingList for use throughout ths class"""
        self.user = User("Esir", "esirkings@gmail.com", "Andela2017")
        self.shopping_list = ShoppingList("Nakkumart", "Close to Town")

    def test_user_can_create_shopping_list(self):
        self.assertEqual(0, len(self.user.shopping_lists))
        self.user.create_shopping_lst(self.shopping_list)
        self.assertEqual(1, len(self.user.shopping_lists))

    def test_user_can_delete_a_shopping_list(self):
        self.assertEqual(0, len(self.user.shopping_lists))
        self.user.create_shopping_lst(self.shopping_list)
        self.assertEqual(1, len(self.user.shopping_lists))
        self.user.delete_shopping_list(self.shopping_list.name)
        self.assertEqual(0, len(self.user.shopping_lists))

    def test_user_delete_unexisting_shopping_list(self):
        self.assertEqual(0, len(self.user.shopping_lists))
        with self.assertRaises(ShoppingListDoesNotExist):
            self.user.delete_shopping_list("wubba_lubba_dub_dub")

    def test_exception_raised_on_try_to_create_similar_shopping_lists(self):
        self.user.create_shopping_lst(self.shopping_list)
        self.user.create_shopping_lst(ShoppingList("wubba_lubba_dub_dub", "Rick And Morty Adventure"))
        with self.assertRaises(ShoppingListAlreadyExist):
            self.user.create_shopping_lst(ShoppingList("wubba_lubba_dub_dub", "Rick And Morty Adventure"))

    def test_get_shopping_list_returns_if_item_found(self):
        """tests if the get.. method in user returns the shoppingList Specified by
        :key and raises (ShoppingListDoesNotExist)exception if not found
        """
        self.user.create_shopping_lst(self.shopping_list)
        self.assertEqual(1, len(self.user.shopping_lists))
        self.assertIsInstance(self.user.get_shopping_lst("Nakkumart"), ShoppingList)
        self.assertEqual("Nakkumart", self.user.get_shopping_lst("Nakkumart").name)
        self.assertEqual(1, len(self.user.shopping_lists))

    def test_get_shoppinglist_raises_exception_if_shoppinglist_not_found(self):
        with self.assertRaises(ShoppingListDoesNotExist):
            self.user.get_shopping_lst("wubba_lubba_dub_dub")

if __name__ == '__main__':
    unittest.main()
