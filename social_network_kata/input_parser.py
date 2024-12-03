import re
from social_network_kata.command import Command
from social_network_kata.command_type import CommandType

class InputParser:

    def __init__(self):
        pass

    def parse_user_input(self, user_input: str) -> Command:
        # Posting: "<user name> -> <message>"
        posting_match = re.match(r"^(\w+) -> (.+)$", user_input)
        
        if posting_match:
            username, message = posting_match.groups()
            return Command(type=CommandType.POSTING, user_name=username, command_input=message)
        else:
            raise NotImplementedError()