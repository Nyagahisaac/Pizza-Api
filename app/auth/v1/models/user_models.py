from sqlalchemy.orm import backref
from app import db

class User(db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    order = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
   

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):

        return f'User {self.name}'

class Restaurant(db.Model):
    __tablename__ = 'hotels'


    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    food = db.Column(db.String(255))
    location = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
   

    def __repr__(self):
        return f'Restaurant {self.name}'

class Food(db.Model):
    __tablename__ = 'food'


    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer(255))
    crust = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
   

    def __repr__(self):
        return f'Food {self.name}'
