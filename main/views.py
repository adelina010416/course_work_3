from json import JSONDecodeError

from flask import render_template, Blueprint, request

from dao.dao import PostDAO
from utils.utils import bookmarks_counter

main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates', static_folder="static")
posts = PostDAO("data/posts.json", "data/comments.json")
comments_amount = posts.change_word_form()


@main_blueprint.route("/")
def feed_page():
    """Лента со всеми постами + форма поиска"""
    return render_template("index.html", bookmarks_amount=bookmarks_counter(), posts=posts.get_posts_all(),
                           comments_amount=comments_amount)


@main_blueprint.route("/posts/<int:post_id>")
def post_page(post_id):
    """Подробный пост + комменты"""
    post = posts.get_post_by_pk(post_id)
    comments = posts.get_comments_by_post_id(post_id)
    return render_template("post.html", post=post, comments_amount=comments_amount, comments=comments)


@main_blueprint.route("/search")
def search_page():
    """Страница поиска"""
    s = request.args.get("s")
    try:
        search_posts = posts.search_for_posts(s)[:10]
        return render_template("search.html", posts=search_posts, posts_amount=len(search_posts),
                               comments_amount=comments_amount)
    except FileNotFoundError or JSONDecodeError:
        return "ошибка загрузки"


@main_blueprint.route("/users/<username>")
def user_page(username):
    """Страница со всеми постами определённого пользователя"""
    user_posts = posts.get_posts_by_user(username)
    return render_template("user_feed.html", posts=user_posts, comments_amount=comments_amount)
