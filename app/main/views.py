import secrets, os
from . import main
from app.models import Comments, Post, User
from app import db
from flask import url_for, render_template, flash, redirect, request, abort
from .forms import PostForm, UpdateAccountForm, CommentForm
from flask_login import  current_user, login_required
from PIL import Image
from app.models import User, Post
from app import db, bcrypt
from flask import url_for, render_template, flash, redirect, request, abort

@main.route("/home")
@main.route("/")
def home():
    post = Post.query.order_by(Post.id.desc())
    return render_template("home.html", posts=post)

@main.route("/new_post", methods=['GET','POST'])
@login_required
def new_post():
   form = PostForm()
   if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been published", "success")

        users = User.query.filter_by(subscribe=True).all()
        for user in users:
            pass
            # mail_message("KK Blog New Article","email/welcome_user",user.email,user=user,blog_title=form.title.data)

        return redirect(url_for('main.home'))
   return render_template("new_post.html",form=form)

@main.route("/post/<id>", methods=['GET','POST'])
@login_required
def post(id):
    form = CommentForm()


    comments = Comments.query.filter_by(post_id=id).all()
    post = Post.query.get_or_404(id)
    return render_template("post.html", title=post.title,post=post, form=form, comments=comments)

@main.route("/post/<post_id>/comment", methods=['GET','POST'])
@login_required
def comment(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comments(post_id=post_id, comment=form.comment.data, user_id=current_user.id)
        db.session.add(new_comment)
        db.session.commit()
        flash("Comment saved!", "success")
    return redirect("/post/"+post_id)



