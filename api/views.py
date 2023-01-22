import logging

from flask import Blueprint, jsonify

from dao.dao import PostDAO

api_blueprint = Blueprint("api_blueprint", __name__, template_folder='templates', static_folder="static")
logging.basicConfig(filename="./logs/api.log", level=logging.INFO, encoding='utf-8',
                    format="%(asctime)s [%(levelname)s] %(message)s")

posts = PostDAO("data/posts.json", "data/comments.json")


@api_blueprint.route("/posts")
def all_posts_json():
    """Возвращает список всех постов в формате json"""
    logging.info("Запрос /api/posts")
    return jsonify(posts.get_all_posts_json())


@api_blueprint.route("/posts/<int:post_id>")
def pk_posts_json(post_id):
    """Возвращает пост по заданному номеру в формате json"""
    logging.info(f"Запрос /api/posts/{post_id}")
    return jsonify(posts.get_by_pk_json(post_id))
