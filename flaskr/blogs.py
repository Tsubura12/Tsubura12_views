from flask import Blueprint, render_template
from flaskr.models import Blog  # Blogモデルをインポート

# Blueprintの作成
blog_bp = Blueprint("blog", __name__)

# /blogs にアクセスしたらDBから全ブログを取得して表示
@blog_bp.route("/blogs")
def blogs():
    # Blogテーブルから全てのデータを取得し、作成日時の降順で並び替え
    blogs_list = Blog.query.order_by(Blog.created_at.desc()).all()
    return render_template('blogs.html', blogs=blogs_list)

# 新規投稿ページ
@blog_bp.route("/blogs/create")
def create():
    return "新規投稿ページです"