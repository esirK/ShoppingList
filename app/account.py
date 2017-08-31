from app.Exceptions import UserAlreadyExist, UserDoesNotExist


class Account(object):
    """ Creates an Account where users can be stored"""

    def __init__(self):
        self.users = {}

    def create_user(self, user):
        """ This Method Creates a User and adds him/her into dict of users """
        if user.id in self.users:
            raise UserAlreadyExist
        else:
            self.users.update({user.id: user})

    def rm_user(self, email):
        """ This Method removes a user from users dictionary using his/her 
        unique email"""
        try:
            self.users.pop(email)
        except KeyError:
            raise UserDoesNotExist

    def check_user(self, email):
        if email in self.users:
            return self.users[email]

    def all_users(self):
        return self.users
