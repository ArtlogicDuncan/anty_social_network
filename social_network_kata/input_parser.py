from social_network_kata.command import Command

class InputParser:

    def __init__(self):
        pass

    def parse_user_input(self, user_input: str) -> Command:
        raise NotImplementedError()