# user model

class User:
    def __init__(self, user_id: str, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password