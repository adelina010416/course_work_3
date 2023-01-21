import json


class PostHandler:
    def __init__(self, path):
        self.path = path

    def get_posts_all(self):
        """Возвращает посты"""
        with open(self.path, "r", encoding="utf-8") as file:
            posts = json.load(file)
        return posts

    def get_posts_by_user(self, user_name):
        """Возвращает посты определенного пользователя.
        Возвращает ошибку 'ValueError', если такого пользователя нет.
         Возвращает пустой список, если у пользователя нет постов."""
        posts = self.get_posts_all()
        user_posts = []
        user_is_exist = False
        for post in posts:
            if user_name.lower() == post["poster_name"].lower():
                user_posts.append(post)
                user_is_exist = True
        if user_is_exist:
            return user_posts
        else:
            raise ValueError("такого пользователя нет :(")

    def search_for_posts(self, query):
        """Возвращает список постов по ключевому слову"""
        posts = []
        for post in self.get_posts_all():
            if query.lower() in post["content"].lower():
                posts.append(post)
        return posts

    def get_post_by_pk(self, pk):
        """Возвращает один пост по его идентификатору"""
        for post in self.get_posts_all():
            if pk == post["pk"]:
                return post

    def get_comments_by_post_id(self, post_id):
        """Возвращает комментарии определенного поста.
        Возвращает ошибку 'ValueError', если такого поста нет.
         Возвращает пустой список, если у поста нет комментов. """
        post_is_exist = 0
        for post in self.get_posts_all():
            if post_id == post["pk"]:
                post_is_exist += 1
        if post_is_exist == 0:
            raise ValueError("такого поста нет :(")
        else:
            with open('data/comments.json', "r", encoding="utf-8") as file:
                comments = json.load(file)
                post_comments = []
                [post_comments.append(comment) for comment in comments if comment["post_id"] == post_id]
            return post_comments
