class ShoppingList:
    def __init__(self, name):
        """ This Class Adds and Manages Items In a User Shopping List"""
        self.name = name
        self.items = {}
        self.categories = {}

    def add_item(self, item):
        self.items.update({item.name: item})

    def remove_item(self, item_name):
        self.items.pop(item_name)

    def update_item(self, item_name, item):
        self.remove_item(item_name)
        self.add_item(item)
