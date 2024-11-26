from social_network_kata.post_repository import PostRepository
from social_network_kata.clock_wrapper import ClockWrapper

class SocialNetworkService:

    def __init__(self, clock: ClockWrapper, repository: PostRepository):
        self.clock = clock

    def add_post(self, user_name: str, content: str):
        raise NotImplementedError