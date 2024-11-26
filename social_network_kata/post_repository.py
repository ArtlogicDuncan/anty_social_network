from social_network_kata.post import Post

class PostRepository:

    def __init__(self) -> None:
        self.posts = list[Post]
    
    def add_post(self, post: Post):
        raise NotImplementedError("PostRepository: add_post()")

    def get_all_posts(self) -> :
        raise NotImplementedError("PostRepository: get_all()")