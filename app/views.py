from flask import render_template
from flask import render_template
from app import posts
from flask import Blueprint, render_template 


views = Blueprint("views", __name__)


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def posts_list():
 return render_template('posts/posts.html')