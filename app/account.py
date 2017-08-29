class Account(object):
    """ Creates an Account where users can be stored"""

    def __init__(self):
        self.users = {}

    def create_user(self, user):
        """ This Method Creates a User and adds him/her into dict of users """
        self.users.update({user.email: user})

    def rm_user(self, email):
        """ This Method removes a user from users dictionary using his/her 
        unique email"""
        self.users.pop(email)

    def all_users(self):
        return self.users
