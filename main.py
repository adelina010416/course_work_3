from flask import Flask, render_template, request
from utils.utils import bookmarks_counter, change_word_form
from utils.posts_handler import PostHandler
from json import JSONDecodeError


app = Flask(__name__)


@app.route("/")
def feed_page():
    posts = PostHandler("data/posts.json")
    comments_amount = change_word_form()
    return render_template("index.html", bookmarks_amount=bookmarks_counter(), posts=posts.get_posts_all(),
                           comments_amount=comments_amount)


@app.route("/posts/<int:post_id>")
def post_page(post_id):
    posts = PostHandler("data/posts.json")
    post = posts.get_post_by_pk(post_id)
    comments_amount = change_word_form()
    comments = posts.get_comments_by_post_id(post_id)
    return render_template("post.html", post=post, comments_amount=comments_amount, comments=comments)


@app.route("/search")
def search_page():
    s = request.args.get("s")
    try:
        posts = PostHandler("data/posts.json")
        posts = posts.search_for_posts(s)[:10]
        return render_template("search.html", posts=posts, posts_amount=len(posts))
    except FileNotFoundError or JSONDecodeError:
        return "ошибка загрузки"


@app.route("/users/<username>")
def user_page(username):
    posts = PostHandler("data/posts.json")
    user_posts = posts.get_posts_by_user(username)
    return render_template("user_feed.html", posts=user_posts)


if __name__ == "__main__":
    app.run(debug=True)
