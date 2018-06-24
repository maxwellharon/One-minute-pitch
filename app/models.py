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
