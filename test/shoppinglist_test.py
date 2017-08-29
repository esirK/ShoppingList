import unittest

from app.ShoppingList import ShoppingList
from app.item import Item


class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.nakkumart = ShoppingList("Nakkumart")

    def test_add_item(self):
        item = Item("Bananas", "Grocery", "10", "5")
        self.assertEqual(0, len(self.nakkumart.items))
        self.nakkumart.add_item(item)
        self.assertEqual(1, len(self.nakkumart.items))

    def test_remove_item(self):
        item = Item("The Flash", "Book", "1000", "1")
        item2 = Item("Call Of Duty", "Game", "3000", "1")
        self.nakkumart.add_item(item)
        self.nakkumart.add_item(item2)
        self.assertEqual(2, len(self.nakkumart.items))
        self.nakkumart.remove_item(item2.name)
        self.assertEqual(1, len(self.nakkumart.items))
        with self.assertRaises(KeyError):
            self.nakkumart.remove_item(item2.name)


if __name__ == '__main__':
    unittest.main()
