# models.py
from myproject import db, login_manager
from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash as cph
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    username = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    avgSpeed = db.Column(db.Integer)
    level = db.Column(db.Integer)
    def __init__(self,name,email,username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password_hash = gph(password)
        self.level = 0
    def check_password(self,password):
        return cph(self.password_hash,password)

# class PracticeLine(db.Model):
#     __tablename__ = 'practicelines'
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(64))
#     def __init__(self,text):
#         self.text = text 
PracticeLine = []
TestLines = []

class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    speed = db.Column(db.Float)
    error = db.Column(db.Integer)
    def __init__(self,text):
        self.text = text 