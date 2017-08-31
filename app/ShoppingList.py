from app.app.Exceptions import ItemDoesNotExist, ItemAlreadyExist


class ShoppingList:
    def __init__(self, name):
        """ This Class Adds and Manages Items In a User Shopping List"""
        self.name = name
        self.items = {}
        self.categories = {}

    def add_item(self, item):
        if item.name in self.items:
            raise ItemAlreadyExist
        else:
            self.items.update({item.name: item})

    def remove_item(self, item_name):
        try:
            self.items.pop(item_name)
        except KeyError:
            raise ItemDoesNotExist

    def update_item(self, item_name, item):
        self.remove_item(item_name)
        self.add_item(item)

    def get_item(self, item_name):
        """Returns an item object whose key is the item_name provided"""
        return self.items[item_name]
