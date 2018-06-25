from flask import render_template,redirect,url_for,flash
from flask_login import login_user,login_required,logout_user
from . import auth
from ..models import User
from .forms import RegistrationForm,LoginForm
from ..import db
from ..import bcrypt
from .. import login_manager
from sqlalchemy import exc


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)


@auth.route('/login',methods=['GET' , 'POST'])
def login():

	"""this function handles login functionalities"""


	login_form = LoginForm()
	if login_form.validate_on_submit():
		user = User.query.filter_by(email=login_form.email.data).first()
		if user and bcrypt.check_password_hash(user.password_hash, login_form.password.data):
			login_user(user,login_form.remember.data)
			# flash("succesifull")
			return redirect(url_for('main.categories'))
		else:
			print("unsuccessful")
	return render_template('auth/login.html', login_form=login_form)



@auth.route('/register', methods=['GET','POST'])
def register():
	"""this function handles registration functionalities"""
	form = RegistrationForm()

	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
		user = User(username=form.username.data,email=form.email.data,password_hash=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash("invalid arguments", "danger")
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', form=form)
