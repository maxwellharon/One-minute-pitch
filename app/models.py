from flask_login import UserMixin
from . import db
from datetime import datetime


class User(UserMixin,db.Model):

	""" This model handles the User model that will be mapped to the database"""

	__tablename__="users"
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(255),index=True)
	email = db.Column(db.String(255), unique=True,index=True)
	bio = db.Column(db.String(255))
	profile_pic_path=db.Column(db.String())
	joined = db.Column(db.DateTime,default=datetime.utcnow)
	password_hash = db.Column(db.String(255))
	pitch = db.relationship('Pitch',backref='author',lazy='dynamic')
	comments = db.relationship('Comment',backref='author',lazy='dynamic')

	def __repr__(self):
		return f"User : {self.username}"


class Pitch(db.Model):

	""" This model handles the Pitch model that will be mapped to the database"""

	__tablename__='pitches'
	id = db.Column(db.Integer,primary_key=True)
	author_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
	body = db.Column(db.Text, index=True)
	timestamp = db.Column(db.DateTime,default=datetime.utcnow)
	upvotes = db.Column(db.Integer, default=int(0))
	downvotes = db.Column(db.Integer, default=int(0))
	category = db.Column(db.String(255), nullable=False)
	comments = db.relationship('Comment',backref='pitch',lazy='dynamic')

	# vote = db.relationship('Vote',backref='pitch',lazy='dynamic')

	def __repr__(self):
		return f'User {self.body}'
