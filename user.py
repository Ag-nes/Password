class User:
    def __init__(self, first_name, last_name, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    user_User = []

    def keep_user(self):

        User.user_User.append(self)

    def delete_user(self):

        User.user_User.remove(self)

    @classmethod
    def display_users(cls):

        return cls.user_User
    @classmethod
    def find_by_name(cls, user_name):
        for user in cls.user_User:
            if user.user_name == user_name:
                return user

    @classmethod
    def user_present(cls, user_name):
        for user in cls.user_User:
            if user.user_name == user_name:
                return True
            return False


    

