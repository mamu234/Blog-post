from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import PasswordField, StringField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length,EqualTo, ValidationError
from ..models import User
from flask_login import current_user



class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    picture=FileField("Update Profile Picture", validators=[FileAllowed(['jpg','png','jpeg'])] )
    submit = SubmitField('Update Post')

    def validate_username(self, username):
        if username.data != current_user.username:
           user = User.query.filter_by(username=username.data).first()
           if user:
               raise ValidationError("Username Taken")
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("Email has already been registered")
      
class PostForm(FlaskForm):
    title=StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit Comment')