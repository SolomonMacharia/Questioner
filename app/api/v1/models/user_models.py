
all_users = []

class User:
    def __init__(self):
        self.db = all_users

    def create_user(self, username, email, password, confirmPassword):
        new_user = {
            "username": username,
            "email": email,
            "password": password,
            "confirmPassword": confirmPassword
        }
        if new_user:
            self.db.append(new_user)
        return new_user

    def get_all_users(self):
        return self.db

    def get_single_user(self, username):
        usr = [usr for usr in all_users if usr[username] == username]
        if usr:
            return usr
        return None

    