import json


def bookmarks_counter():
    """Возвращает количество закладок"""
    with open("data/bookmarks.json", "r", encoding="utf-8") as file:
        bookmarks = json.load(file)
        return len(bookmarks)


def get_comments(post_id):
    """Возвращает список комментариев к определённому посту и длину этого списка"""
    with open("data/comments.json", "r", encoding="utf-8") as file:
        comments = json.load(file)
        post_comments = []
        for comment in comments:
            if comment["post_id"] == post_id:
                post_comments.append(comment)
        comments_amount = len(post_comments)
    return post_comments, comments_amount


def comments_counter():
    """Возвращает список с количеством комментов к каждому посту"""
    with open("data/posts.json", "r", encoding="utf-8") as file:
        posts = json.load(file)
        posts_amount = len(posts)
    amount_list = []
    for i in range(1, posts_amount + 1):
        comments, amount = get_comments(i)
        amount_list.append(amount)
    return amount_list


def change_word_form():
    """Склоняет слово 'комментарий'"""
    amount_list = comments_counter()
    result_list = []
    for i in amount_list:
        if int(str(i)[-1]) in range(5, 10) or int(str(i)[-2:]) in range(11, 20) or str(i).endswith("0"):
            result_list.append(f"{i} комментариев")
        elif int(str(i)[-1]) in range(2, 5):
            result_list.append(f"{i} комментария")
        elif str(i).endswith("1"):
            result_list.append(f"{i} комментарий")
    return result_list
