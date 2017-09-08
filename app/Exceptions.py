class ItemDoesNotExist(Exception):
    """If an Item Does Not Exist This Exception is Raised"""
    pass


class ItemAlreadyExist(Exception):
    """If an Item Does Exist This Exception is Raised"""
    pass


class UserAlreadyExist(Exception):
    """If a User Does Exist This Exception is Raised"""
    pass


class UserDoesNotExist(Exception):
    """If a User Does Not Exist This Exception is Raised"""
    pass


class ShoppingListDoesNotExist(Exception):
    """Raised If A non-existing ShoppingList is tried to be removed from a user
    shopping List
    """
    pass


class ShoppingListAlreadyExist(Exception):
    """Raised on Attempt to add a shopping list with same manes"""
    pass
