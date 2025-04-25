from util import db_connection
from exception.custom_exceptions import UserAlreadyExistsException

class FacultyDAO:
    def __init__(self):
        self.db = db_connection.get_db()

    def add_faculty(self, data):
        faculty_collection = self.db.faculty
        if faculty_collection.find_one({'email': data.get('email')}):
            raise UserAlreadyExistsException('Faculty with this email already exists')
        faculty_collection.insert_one(data)
