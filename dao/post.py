class Post:
    def __init__(self, poster_name, poster_avatar, pic, content, views_count, likes_count, pk):
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count
        self.pk = pk

    def __repr__(self):
        return f"{self.poster_name}, номер поста {self.pk}"

    def __eq__(self, other):
        if isinstance(other, Post):
            return (self.poster_name == other.poster_name and
                    self.poster_avatar == other.poster_avatar and
                    self.pic == other.pic and
                    self.content == other.content and
                    self.views_count == other.views_count and
                    self.likes_count == other.likes_count and
                    self.pk == other.pk)
        return NotImplemented
