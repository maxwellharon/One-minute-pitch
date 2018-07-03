from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class CategoryForm(FlaskForm):
    """
    class to create a form to create category
    """
    name = StringField('Pitch Category',validators=[Required()])
    submit = SubmitField('Create')


class PitchForm(FlaskForm):
    """
    class to create form to write pitch
    """
    pitch = StringField('Pitch Content', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    """
    class to create form to comment on a pitch
    """
    comment = StringField('Comment Content', validators=[Required()])
    submit = SubmitField('Submit')
