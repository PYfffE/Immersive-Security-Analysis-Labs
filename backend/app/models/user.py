class User:
    def __init__(self, user_id: str, username, password, admin):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.is_admin = admin

    def check_password(self, password):
        return self.password == password
