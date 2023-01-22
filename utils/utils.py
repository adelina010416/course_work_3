import json


def bookmarks_counter():
    """Возвращает количество закладок"""
    with open("data/bookmarks.json", "r", encoding="utf-8") as file:
        bookmarks = json.load(file)
        return len(bookmarks)
