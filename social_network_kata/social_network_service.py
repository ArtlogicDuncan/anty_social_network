from social_network_kata.clock_wrapper import ClockWrapper

class SocialNetworkService:

    def __init__(self, clock: ClockWrapper):
        self.clock = clock

    def add_post(self):
        raise NotImplementedError