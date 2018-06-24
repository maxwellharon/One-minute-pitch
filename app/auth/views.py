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
