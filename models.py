from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    """Simple user model for authentication."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def get_id(self):
        return str(self.id)


def get_user_by_username(username):
    """Return a user by username."""
    if not username:
        return None
    return User.query.filter_by(username=username).first()


def get_user_by_id(user_id):
    """Return a user by id."""
    if not user_id:
        return None
    return User.query.get(int(user_id))


def create_user(username, password):
    """Create and return a new user."""
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return user

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
