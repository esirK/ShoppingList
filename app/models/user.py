from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.Exceptions import ShoppingListDoesNotExist, ShoppingListAlreadyExist


class User(UserMixin):
    def __init__(self, name, email, password):
        self.password_hash = generate_password_hash(password)
        self.name = name
        self.id = email
        self.shopping_lists = {}

    def __name__(self):
        return self.name

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def create_shopping_lst(self, shopping_lst):
        """ 
        This Method adds shopping_list into the current user shopping lists
        """
        if shopping_lst.name in self.shopping_lists:
            raise ShoppingListAlreadyExist(shopping_lst.name
                                           + " Had been Created")
        self.shopping_lists.update({shopping_lst.name: shopping_lst})

    def delete_shopping_list(self, shopping_lst_name):
        """' 
        This Method removes a shopping_list from the current user shopping lists

        """
        try:
            self.shopping_lists.pop(shopping_lst_name)
        except KeyError:
            raise ShoppingListDoesNotExist

    def get_shopping_lst(self, shopping_lst_name):
        """ 
        Returns a shopping_list by name the name of 'shopping_lst_name
         """
        try:
            self.shopping_lists[shopping_lst_name]
        except KeyError:
            raise ShoppingListDoesNotExist
        return self.shopping_lists[shopping_lst_name]

    def update_shopping_list(self, shopping_list):
        """
        This method takes in 
        :param shopping_list:
        and updates the shopping list 
        """
        self.delete_shopping_list(shopping_list.name)
        self.create_shopping_lst(shopping_list)

    def get_num_of_shopping_lists(self):
        return len(self.shopping_lists)
