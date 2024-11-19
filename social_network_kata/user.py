from social_network_kata.post import Post

class User:
    ID = str

    def __init__(self, id: ID, posts: list[Post] = []):
        self.id = id
        self.posts = posts
        pass
    