from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Category, Pitch, Comment
from .forms import CategoryForm,PitchForm,CommentForm
from flask_login import login_required,current_user
# from ..models import Category



# Views
@main.route('/')
def index():
    """
    View root page for the application
    :return:
    """
    categories = Category.get_categories()
    title = 'Home'
    return render_template('index.html', title=title, categories=categories)

@main.route('/category/new', methods=['GET', 'POST'])
@login_required
def new_category():
    form = CategoryForm()
    if form.validate_on_submit():
        name = form.name.data
        new_category = Category(name=name)
        new_category.save_category()
        return redirect(url_for('.index'))
    title = 'New Pitch Category'
    return render_template('new_category.html', category_form=form)


@main.route('/category/<int:id>')
def category(id):
    category = Category.query.get(id)
    pitch = Pitch.query.filter_by(category_id=id)

    title = f'{category.name} page'

    return render_template('category.html',title=title, category=category,pitch=pitch)

@main.route('/category/pitch/new/<int:id>', methods=['GET', 'POST'])

@login_required
def new_pitch(id):
    category = Category.query.get(id)
    form = PitchForm()
    if form.validate_on_submit():
        pitch = form.pitch.data
        new_pitch = Pitch(pitch=pitch, user=current_user, category_id=id)
        new_pitch.save_pitch()
        return redirect(url_for('.category', id=id))

    title = 'New Pitch'
    return render_template('new_pitch.html', title=title, pitch_form=form)


@main.route('/pitch/<int:id>')
def pitch(id):
    pitch = Pitch.query.get(id)
    comment = Comment.get_comments(pitch_id=id)

    # Comment.query.order_by(Comment.id.desc()).filter_by(pitch_id=id).all()

    title = f'Pitch { pitch.id }'
    return render_template('pitch.html',title=title, pitch=pitch, comment=comment)


@main.route('/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    pitch = Pitch.query.get(id)
    # comment = Comment.query.get(pitch_id)

    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment=comment, user=current_user, pitch_id=id)
        new_comment.save_comment()
        return redirect(url_for('.pitch', id=id))
    # title = f' Comment{comment.id}'
    return render_template('new_comment.html', comment_form=form, pitch=pitch)



# @main.route('/test/<int:id>')
# def comment(id):
#     comment = Comment.query.get(id)
#
#     # title = f'Comment { comments.id }'
#     return render_template('test.html', comment=comment, )
