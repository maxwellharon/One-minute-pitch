from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
# from ..models import User


class UpdateProfile(FlaskForm):
	bio = TextAreaField("Tell us about you.", validators=[Required()])
	submit = SubmitField('submit')


class PitchForm(FlaskForm):
	body = TextAreaField("whats your pitch ?",validators=[Required()])
	category = RadioField('Label', choices=[('pickup lines','pickup lines'), ('interview pitch','interview pitch'),('product pitch','product pitch'),('promotion pitch','promotion pitch')])
	submit = SubmitField('Submit')
