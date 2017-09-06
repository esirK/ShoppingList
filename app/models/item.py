class Item:
    def __init__(self, name, price, quantity, category=None):
        self.name = name
        self.price = price
        self.quantity = quantity

        if category is None:
            self.category = "General"
        else:
            self.category = category

    def __eq__(self, other):
        if self.name == other.name and self.price == other.price and \
                        self.quantity == other.quantity and self.category == other.category:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
