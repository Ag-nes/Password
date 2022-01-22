from credentials import Credentials
from user import User

def create_user(first_name, last_name, user_name, password):
    user =  User(first_name, last_name, user_name, password)
    return user

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()



