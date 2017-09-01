from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, name, email, password):
        self.name = name
        self.id = email
        self.password = password
        self.shopping_lists = {}

    def __name__(self):
        return self.name

    def create_shopping_lst(self, shopping_lst):
        """' This Method adds shopping_list into the current user shopping lists"""
        self.shopping_lists.update({shopping_lst.name: shopping_lst})

    def delete_shopping_list(self, shopping_lst_name):
        """' This Method removes a shopping_list from the current user shopping lists"""
        self.shopping_lists.pop(shopping_lst_name)

    def get_shopping_lst(self, shopping_lst_name):
        """ Returns a shopping_list by name the name of 'shopping_lst_name' """
        return self.shopping_lists[shopping_lst_name]
