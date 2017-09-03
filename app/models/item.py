class Item:
    def __init__(self, name, price, quantity, category=None):
        self.name = name
        self.price = price
        self.quantity = quantity

        if category is None:
            self.category = "General"
        else:
            self.category = category
