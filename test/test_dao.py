import json

import pytest

from dao.dao import PostDAO
from dao.post import Post

posts = PostDAO("data/posts.json", "data/comments.json")


@pytest.fixture()
def posts_list():
    with open("data/posts.json", "r", encoding="utf-8") as file:
        posts_f = json.load(file)
    return posts_f


leo_posts = [Post("leo", "https://randus.org/avatars/w/c1819dbdffffff18.png",
                  "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
                  "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
                  376,
                  154,
                  1),
             Post("leo", "https://randus.org/avatars/w/c1819dbdffffff18.png",
                  "https://images.unsplash.com/photo-1570427968906-5a309bfd7de3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80",
                  "Пурр-пурр! типичная инстарамная фотка с котом , книжкой и едой. Но не буду скрывать, что это я: а то вдруг у вас кот тоже такой, тогда вы не увидите этого в своих фото. #кот #котики #инста #инстаграм #любовькживотным #любимыйкот ... Как же я люблю этот момент, когда ты понимаешь, что ты ничего толком не умеешь делать и даже не знаешь, что с этим делать.",
                  287,
                  99,
                  5)]

hank_posts = [Post("hank", "https://randus.org/avatars/m/383c7e7e3c3c1818.png",
                   "https://images.unsplash.com/photo-1612450632008-22c2a5437dc1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
                   "Смотрите-ка – ржавые елки! Раньше на этом месте была свалка старых машин, а потом все засыпали песком. Теперь тут ничего не растет – только ржавые елки , кусты и грязь. Да и не может тут ничего расти: слишком много пыли и песка. Зато теперь стало очень красиво – все-таки это не свалка.",
                   187,
                   67,
                   3),
              Post("hank", "https://randus.org/avatars/m/383c7e7e3c3c1818.png",
                   "https://images.unsplash.com/photo-1494548162494-384bba4ab999?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80",
                   "Очень красивый закат. Стоило выбраться из дома, чтобы посмотреть на него! а где ты был?",
                   166,
                   76,
                   7)]
hank_post = hank_posts[0]
leo_post = leo_posts[0]
hank_post_list = [hank_posts[0]]
leo_post_list = [leo_posts[0]]

comment_6 = [{"post_id": 6, "commenter_name": "larry", "comment": "Класс!", "pk": 19}]
comment_7 = [{"post_id": 7, "commenter_name": "hanna", "comment": "Очень необычная фотография! Где это?", "pk": 20}]


class TestPost:
    def test_get_posts_all(self, posts_list):
        assert posts.get_all_posts_json() == posts_list, "неверно для get_posts_all"

    @pytest.mark.parametrize("name, result", [("leo", leo_posts), ("hank", hank_posts)])
    def test_get_posts_by_user(self, name, result):
        assert posts.get_posts_by_user(name) == result, f"неверно для get_posts_by_user '{name}'"

    def test_get_post_by_user_mistake(self):
        with pytest.raises(ValueError):
            posts.get_posts_by_user("Adeline")

    @pytest.mark.parametrize("post_id, result", [(6, comment_6), (7, comment_7)])
    def test_get_comments_by_post_id(self, post_id, result):
        assert posts.get_comments_by_post_id(post_id) == result, f"неверно для get_comments_by_post_id '{post_id}'"

    def test_get_comments_by_post_id_mistake(self):
        with pytest.raises(ValueError):
            posts.get_comments_by_post_id(0)

    @pytest.mark.parametrize("query, result", [("квадратная", leo_post_list), ("ржавые", hank_post_list), ("4", [])])
    def test_search_for_posts(self, query, result):
        assert posts.search_for_posts(query) == result, f"неверно для search_for_posts '{query}'"

    @pytest.mark.parametrize("pk, result", [(1, leo_post), (3, hank_post)])
    def test_get_post_by_pk(self, pk, result):
        assert posts.get_post_by_pk(pk) == result, f"неверно для get_post_by_pk '{pk}'"
