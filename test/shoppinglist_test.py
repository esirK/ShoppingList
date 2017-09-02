import unittest

from app.Exceptions import ItemDoesNotExist, ItemAlreadyExist
from app.models.ShoppingList import ShoppingList
from app.models.item import Item


class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.nakkumart = ShoppingList("Nakkumart", " The Supermarket Is Close")
        self.item = Item("Call Of Duty", "Game", 3000, 1)

    def test_add_item(self):
        item = Item("Bananas", "Grocery", 10, 5)
        self.assertEqual(0, len(self.nakkumart.items))
        self.nakkumart.add_item(item)
        self.assertEqual(1, len(self.nakkumart.items))

    def test_remove_item(self):
        item = Item("The Flash", "Book", 1000, 1)
        item2 = Item("Call Of Duty", "Game", 3000, 1)
        self.nakkumart.add_item(item)
        self.nakkumart.add_item(item2)
        self.assertEqual(2, len(self.nakkumart.items))
        self.nakkumart.remove_item(item2.name)
        self.assertEqual(1, len(self.nakkumart.items))

    def test_exception_raised_if_non_existing_item_is_removed(self):
        item = Item("The Flash", "Book", 1000, 1)  # Item not yet added to shopping list
        with self.assertRaises(ItemDoesNotExist):
            self.nakkumart.remove_item(item.name)

    def test_update_item(self):
        item = Item("Call Of Duty", "Game", 3000, 1)
        self.nakkumart.add_item(item)
        self.assertEqual(item.price, self.nakkumart.get_item(item.name).price)
        updated_item = Item("Call Of Duty", "Game", 3500, 1)
        self.nakkumart.update_item(item.name, updated_item)
        self.assertEqual(updated_item.price, self.nakkumart.get_item(item.name).price)

    def test_updating_an_item_not_in_shopping_list_raises_exception(self):
        with self.assertRaises(ItemDoesNotExist):
            self.nakkumart.update_item("War Zone", self.item)

    def test_adding_existing_item_raises_exception(self):
        self.nakkumart.add_item(self.item)
        new_item = Item("Call Of Duty", "Movie", 4000, 3)  # Item With same name as Item
        with self.assertRaises(ItemAlreadyExist):
            self.nakkumart.add_item(new_item)


if __name__ == '__main__':
    unittest.main()
