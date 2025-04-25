from util import db_connection
from exception.custom_exceptions import UserNotFoundException

class LoginDAO:
    def __init__(self):
        self.db = db_connection.get_db()

    def add_login(self, data):
        login_collection = self.db.login
        login_collection.insert_one(data)

    def verify_login(self, email):
        login_collection = self.db.login
        user = login_collection.find_one({'email': email})
        if not user:
            raise UserNotFoundException('User not found')
        return user
