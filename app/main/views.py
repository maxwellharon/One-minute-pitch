from flask import render_template,request,redirect,url_for,abort,flash
from flask_login import login_required,current_user
from flask.views import View,MethodView
from . import main
from ..models import *
from .forms import *
from .. import db,photos
from .. import socketio,send



class IndexView(View):
	decorators=[login_required,]

	def __init__(self,template_name):
		self.template_name = template_name

	def dispatch_request(self):
		form = PitchForm()
		if form.validate_on_submit():
			pitch = Pitch(body=form.body.data, author=current_user._get_current_object(),category=form.category.data)
			db.session.add(pitch)
			db.session.commit()
			return redirect(url_for('main.index'))
		pitches = Pitch.query.order_by(Pitch.timestamp.desc()).all()


		return render_template(self.template_name,form=form, pitches=pitches)

main.add_url_rule('/', view_func=IndexView.as_view('index', template_name='index.html'),methods=["GET","POST"])


class ProfileView(MethodView):
	decorators=[login_required,]

	def __init__(self,template_name):
		self.template_name = template_name


	def get(self, uname):
		if uname is None:
			# pass
			abort(404)
		else:
			self.user = User.query.filter_by(username=uname).first()
			self.pitches = Pitch.query.filter_by(author_id=self.user.id).all()
			return render_template(self.template_name, user=self.user,pitches=self.pitches)
