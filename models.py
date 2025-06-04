from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from flask_login import UserMixin

# Dummy in-memory user store (replace with DB later)
users = {
    'admin': {'id': 1, 'username': 'admin', 'password': 'admin123'},
}

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def get_id(self):
        return str(self.id)

def get_user_by_username(username):
    user_data = users.get(username)
    if user_data:
        return User(**user_data)
    return None

def get_user_by_id(user_id):
    for user_data in users.values():
        if str(user_data['id']) == str(user_id):
            return User(**user_data)
    return None

class HCSubscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(100))
    active = db.Column(db.Boolean)

class SubmitProblemsTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(100))
    grade = db.Column(db.Integer)
    concept = db.Column(db.String(100))
    correct = db.Column(db.Boolean)
    HCScore = db.Column(db.Integer)

class TestsMaster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(100))
    sub_concept = db.Column(db.String(100))
    grade = db.Column(db.Integer)
    status = db.Column(db.String(50))
    create_date = db.Column(db.DateTime)
