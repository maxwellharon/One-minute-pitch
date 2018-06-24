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

profile_view = ProfileView.as_view('profile',template_name="profile/profile.html")
main.add_url_rule('/user/<uname>/', view_func=profile_view)
main.add_url_rule('/user/', defaults={'uname':None}, view_func=profile_view, methods=["GET",])


class PitchView(View):
	decorators=[login_required,]

	def __init__(self,template_name):
		self.template_name = template_name

	def dispatch_request(self,id):
		pitch = Pitch.query.get_or_404(id)
		form = CommentForm()
		if form.validate_on_submit():
			comment = Comment(body=form.body.data,pitch=pitch,author=current_user._get_current_object())

			db.session.add(comment)
			db.session.commit()
			flash('your comment has been added','success')
			return redirect(url_for('main.index',id=pitch.id))
		comments = Comment.query.filter_by(pitch_id=id).all()
		user = User.query.filter_by(id=Comment.author_id).first()


		return render_template(self.template_name,form=form,pitch=pitch,comments=comments,user=user)

main.add_url_rule('/pitch/<int:id>/', view_func=PitchView.as_view('pitch', template_name='pitch.html'),methods=["GET","POST"])


@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
	user = User.query.filter_by(username=uname).first()
	if user is None:
		abort(404)

	form = UpdateProfile()
	if form.validate_on_submit():
		user.bio = form.bio.data

		db.session.add(user)
		db.session.commit()

		return redirect(url_for('main.profile',uname=user.username))
	return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/upadate/pic',methods=['GET','POST'])
@login_required
def update_pic(uname):
	user = User.query.filter_by(username=uname).first()
	if 'photo' in request.files:
		filename = photos.save(request.files['photo'])
		path = f"photos/{filename}"
		user.profile_pic_path=path
		db.session.commit()
	return redirect(url_for('main.profile',uname=uname))
