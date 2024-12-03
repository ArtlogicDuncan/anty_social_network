from social_network_kata.post_repository import PostRepository
from social_network_kata.clock_wrapper import ClockWrapper
from social_network_kata.post import Post

class SocialNetworkService:

    def __init__(self, clock: ClockWrapper, post_repository: PostRepository):
        self.clock = clock
        self.post_repository = post_repository

    def add_post(self, user_name: str, content: str):
        created_at = self.clock.get_time()
        post = Post(user_name, content, created_at)
        self.post_repository.add_post(post)

    def get_posts_for_username(self, user_name: str):
        raise NotImplementedError(user_name)
