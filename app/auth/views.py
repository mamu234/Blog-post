from flask_bcrypt import check_password_hash
import secrets, os, app
from . import auth
from sqlalchemy.orm import query
from app.models import User, Post
from app import db, bcrypt
from flask import url_for, render_template, flash, redirect, request, abort
from .formsauth import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required


@auth.route("/signup", methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    reg_form = RegistrationForm()
    log_form = LoginForm()
    if reg_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(reg_form.password.data).decode('utf-8')
        user = User(username = reg_form.username.data, email=reg_form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Created successfully", "success")
        return redirect(url_for('auth.login'))
    return render_template("registerLogin.html", reg_form=reg_form, log_form=log_form)



@auth.route("/login", methods=['GET','POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    reg_form = RegistrationForm()
    log_form = LoginForm()
    if log_form.validate_on_submit():
        user = User.query.filter_by(email=log_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, log_form.password.data):
                login_user(user, remember=log_form.remember.data)
                next_page = request.args.get('next')  
                flash(f"LoggedIn!", "success")
                return redirect(next_page) if next_page else redirect(url_for("main.home"))
        else:
            flash(f"Invalid credentials", "danger")
        
    return render_template("registerLogin.html", log_form=log_form, reg_form=reg_form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))
