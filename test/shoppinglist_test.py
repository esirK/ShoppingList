import unittest

from app.Exceptions import ItemDoesNotExist, ItemAlreadyExist
from app.models.ShoppingList import ShoppingList
from app.models.item import Item


class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.nakkumart = ShoppingList("Nakkumart", " The Supermarket Is Close")
        self.cod = Item("Call Of Duty", 3000, 1, "Game")
        self.morty = Item("WabbDabDah", 3000, 1, "Game")
        self.rick = Item("Ricky And Morty", 3000, 1, "Book")

    def test_add_item(self):
        # No Categories where a user can keep his or her items by default

        self.assertEqual(0, len(self.nakkumart.categories))
        self.nakkumart.add_item(self.cod)
        # on Add item a Category called Game is created where the call_of_duty games
        #  are stored into

        # len of categories should remain 1
        self.nakkumart.add_item(self.morty)
        self.assertEqual(1, len(self.nakkumart.categories))

        # len of the Grocery category should now be 2
        self.assertEqual(2, len(self.nakkumart.categories[self.morty.category]))

    def test_remove_item(self):
        self.nakkumart.add_item(self.cod)
        self.nakkumart.add_item(self.rick)

        # Category for Book and Category For Game
        self.assertEqual(2, len(self.nakkumart.categories))
        self.nakkumart.remove_item(self.cod)
        # Will remove the book "The Flash" and Books category also"
        self.assertEqual(1, len(self.nakkumart.categories))

    def test_category_removed_if_its_empty(self):
        self.nakkumart.add_item(self.cod)
        self.assertEqual(1, len(self.nakkumart.categories))
        self.nakkumart.remove_item(self.cod)
        # Check if "Game" category is removed if it has no items
        self.assertEqual(0, len(self.nakkumart.categories))

    def test_exception_raised_if_non_existing_item_is_removed(self):
        item = Item("The Flash", 1000, 1, "Book")
        # Item not yet added to shopping list
        with self.assertRaises(ItemDoesNotExist):
            self.nakkumart.remove_item(item)

    def test_update_item(self):
        self.nakkumart.add_item(self.cod)
        updated_item = Item("Call Of Duty", 3500, 1, "Game")
        self.nakkumart.update_item(updated_item)
        self.assertEqual(updated_item.price,
                         self.nakkumart.get_item(self.cod).price)

    def test_updating_an_item_not_in_shopping_list_raises_exception(self):
        with self.assertRaises(ItemDoesNotExist):
            self.nakkumart.update_item(self.cod)

    def test_adding_existing_item_raises_exception(self):
        self.nakkumart.add_item(self.cod)
        self.nakkumart.add_item(self.morty)
        with self.assertRaises(ItemAlreadyExist):
            self.nakkumart.add_item(self.morty)

    def test_if_no_item_category_provided_general_category_is_used(self):
        """
        This Method Test if the user doesn't have the ability to categorize
        an item then the item is added to a default (general) category
        """
        general_item = Item("Mysterious Item", 5300, 1)
        # Before adding the Item No Category so len == 0
        self.assertTrue("General", general_item.category)
        self.assertEqual(0, len(self.nakkumart.categories))
        self.nakkumart.add_item(general_item)
        self.assertEqual(1, len(self.nakkumart.categories))


if __name__ == '__main__':
    unittest.main()
