from flask import Blueprint, render_template, request, redirect, url_for, flash # <= ここを追加
from flaskr import db
# models.pyのBlogクラスをインポート
from flaskr.models import Blog

blog_bp = Blueprint('blogs', __name__, url_prefix='/blogs') # <= ここを変更

# 一覧表示
@blog_bp.route('/')
def index():
    blogs = Blog.query.order_by(Blog.created_at.desc()).all()
    return render_template('blogs/index.html', blogs=blogs) # <= テンプレートパスを変更を追加
