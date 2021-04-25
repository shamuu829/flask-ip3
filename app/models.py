from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

#...
@login_manager.user_loader
def load_user(id):
        return User.query.get(int(id))
        
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref = 'use', lazy = 'dynamic')
    comments = db.relationship('Comment', backref = 'comment1', lazy = 'dynamic')
    # like = db.relationship('Like', backref = 'like1', lazy = 'dynamic')
    # dislike = db.relationship('Dislike', backref = 'dislike1', lazy = 'dynamic')

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    
    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitch'
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    category= db.Column(db.String(255),index = True)
    content= db.Column(db.String(255)) 
    comments = db.relationship('Comment', backref = 'pitch1', lazy = 'dynamic')
    # like = db.relationship('Like', backref = 'pitch2', lazy = 'dynamic')
    # dislike = db.relationship('Dislike', backref = 'pitch3', lazy = 'dynamic')

    def __repr__(self):
        return f'pitch {self.content}'  

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey ('pitch.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    content= db.Column(db.String(255)) 

    def __repr__(self):
        return f'Comment :content {self.content}' 