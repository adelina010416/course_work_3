import json

import pytest

from utils.posts_handler import PostHandler


@pytest.fixture()
def posts_list():
    with open("data/posts.json", "r", encoding="utf-8") as file:
        posts = json.load(file)
    return posts


@pytest.fixture()
def leo_posts():
    return [posts_list[0], posts_list[4]]


@pytest.fixture()
def hank_posts():
    return [posts_list[2], posts_list[6]]


@pytest.fixture()
def comments_id_6():
    return [{"post_id": 6, "commenter_name": "larry", "comment": "Класс!", "pk": 19}]


@pytest.fixture()
def comments_id_7():
    return [{"post_id": 7, "commenter_name": "hanna", "comment": "Очень необычная фотография! Где это?", "pk": 20}]


@pytest.fixture()
def post_1():
    with open('../data/posts.json', "r", encoding="utf-8") as file:
        posts = json.load(file)
    return posts[0]


@pytest.fixture()
def post_3():
    return [{
        "poster_name": "hank",
        "poster_avatar": "https://randus.org/avatars/m/383c7e7e3c3c1818.png",
        "pic":
            "https://images.unsplash.com/photo-1612450632008-22c2a5437dc1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
        "content": "Смотрите-ка – ржавые елки! Раньше на этом месте была свалка старых машин, "
                   "а потом все засыпали песком. Теперь тут ничего не растет – только ржавые елки , кусты и грязь. "
                   "Да и не может тут ничего расти: слишком много пыли и песка. Зато теперь стало очень красиво – "
                   "все-таки это не свалка.",
        "views_count": 187,
        "likes_count": 67,
        "pk": 3
    }]


class TestPostHandler:
    def test_get_posts_all(self, posts_list):
        posts = PostHandler("data/posts.json")
        assert posts.get_posts_all() == posts_list, "неверно для get_posts_all"

    @pytest.mark.parametrize("name, result", [("leo", leo_posts), ("hank", hank_posts)])
    def test_get_posts_by_user(self, name, result):
        posts = PostHandler("data/posts.json")
        assert posts.get_posts_by_user(name) == result, f"неверно для get_posts_by_user '{name}'"

    def test_get_post_by_user_mistake(self):
        with pytest.raises(ValueError):
            posts = PostHandler("data/posts.json")
            posts.get_posts_by_user("Adeline")

    @pytest.mark.parametrize("post_id, result", [(6, comments_id_6), (7, comments_id_7)])
    def test_get_comments_by_post_id(self, post_id, result):
        posts = PostHandler("data/posts.json")
        assert posts.get_comments_by_post_id(post_id) == result, f"неверно для get_comments_by_post_id '{post_id}'"

    def test_get_comments_by_post_id_mistake(self):
        with pytest.raises(ValueError):
            posts = PostHandler("data/posts.json")
            posts.get_comments_by_post_id(0)

    @pytest.mark.parametrize("query, result", [("квадратная", post_1), ("ржавые", post_3), ("4", [])])
    def test_search_for_posts(self, query, result):
        posts = PostHandler("data/posts.json")
        assert posts.search_for_posts(query) == result, f"неверно для search_for_posts '{query}'"

    @pytest.mark.parametrize("pk, result", [(1, post_1), (3, post_3)])
    def test_get_post_by_pk(self, pk, result):
        posts = PostHandler("data/posts.json")
        assert posts.get_post_by_pk(pk) == result, f"неверно для get_post_by_pk '{pk}'"

