from social_network_kata.input_parser import InputParser
from social_network_kata.command import Command
from social_network_kata.command_type import CommandType

class TestInputParser:

    def test_parse_post_command(self):
        input_parser = InputParser()
        user_name = "PrincessAtta"
        post_content = "The caterpillar's using himself as live bait"

        command = input_parser.parse_user_input(f"{user_name} -> {post_content}")

        assert command == Command(type=CommandType.POSTING, user_name=user_name, command_input=post_content)

    def test_can_get_posts_for_username(self):
        input_parser = InputParser()
        user_name = "PrincessAtta"

        command = input_parser.parse_user_input(user_name)

        assert command == Command(type=CommandType.READING, user_name=user_name)