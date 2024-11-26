from social_network_kata.post import Post

class PostRepository:

    def __init__(self) -> None:
        self.posts: list[Post] = []
    
    def add_post(self, post: Post) -> None:
        self.posts.append(post)

    def get_all_posts(self) -> list[Post]:
        return self.posts