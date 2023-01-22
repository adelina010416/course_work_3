import json

from dao.post import Post


class PostDAO:
    def __init__(self, posts_path, comments_path):
        self.posts_path = posts_path
        self.comments_path = comments_path

    def get_posts_all(self):
        """Возвращает список объектов класса Post"""
        with open(self.posts_path, "r", encoding="utf-8") as file:
            new_posts = []
            posts = json.load(file)
            for post in posts:
                new_posts.append(Post(post["poster_name"],
                                      post["poster_avatar"],
                                      post["pic"],
                                      post["content"],
                                      post["views_count"],
                                      post["likes_count"],
                                      post["pk"]))
            return new_posts

    def get_posts_by_user(self, user_name):
        """Возвращает посты определенного пользователя.
        Возвращает ошибку 'ValueError', если такого пользователя нет.
         Возвращает пустой список, если у пользователя нет постов.
         Args:
             user_name: имя пользователя"""
        posts = self.get_posts_all()
        user_posts = []
        user_is_exist = False
        for post in posts:
            if user_name.lower() == post.poster_name.lower():
                user_posts.append(post)
                user_is_exist = True
        if user_is_exist:
            return user_posts
        else:
            raise ValueError("такого пользователя нет :(")

    def search_for_posts(self, query):
        """Возвращает список постов по ключевому слову
        Args:
            query: ключевое слово для поиска"""
        posts = []
        for post in self.get_posts_all():
            if query.lower() in post.content.lower():
                posts.append(post)
        return posts

    def get_post_by_pk(self, pk):
        """Возвращает один пост по его идентификатору
        Args:
            pk: номер поста"""
        for post in self.get_posts_all():
            if pk == post.pk:
                return post

    def get_comments(self):
        """Возвращает список комментариев"""
        with open(self.comments_path, "r", encoding="utf-8") as file:
            comments = json.load(file)
            return comments

    def get_comments_by_post_id(self, post_id):
        """Возвращает комментарии определенного поста.
        Возвращает ошибку 'ValueError', если такого поста нет.
         Возвращает пустой список, если у поста нет комментов.
         Args:
             post_id: номер поста"""
        post_is_exist = 0
        for post in self.get_posts_all():
            if post_id == post.pk:
                post_is_exist += 1
        if post_is_exist == 0:
            raise ValueError("такого поста нет :(")
        else:
            comments = self.get_comments()
            post_comments = []
            [post_comments.append(comment) for comment in comments if comment["post_id"] == post_id]
            return post_comments

    def comments_counter(self):
        """Возвращает список с количеством комментов к каждому посту"""
        posts = self.get_posts_all()
        posts_amount = len(posts)
        amount_list = []
        for i in range(1, posts_amount + 1):
            amount = len(self.get_comments_by_post_id(i))
            amount_list.append(amount)
        return amount_list

    def change_word_form(self):
        """Склоняет слово 'комментарий'"""
        amount_list = self.comments_counter()
        result_list = []
        for i in amount_list:
            if int(str(i)[-1]) in range(5, 10) or int(str(i)[-2:]) in range(11, 20) or str(i).endswith("0"):
                result_list.append(f"{i} комментариев")
            elif int(str(i)[-1]) in range(2, 5):
                result_list.append(f"{i} комментария")
            elif str(i).endswith("1"):
                result_list.append(f"{i} комментарий")
        return result_list

    def get_all_posts_json(self):
        """Возвращает список постов в формате json"""
        with open(self.posts_path, "r", encoding="utf-8") as file:
            posts = json.load(file)
        return posts

    def get_by_pk_json(self, pk):
        """Возвращает пост по его номеру в формате json"""
        posts = self.get_all_posts_json()
        for post in posts:
            if post["pk"] == pk:
                return post
