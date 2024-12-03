from unittest.mock import patch, Mock

from social_network_kata.input_wrapper import InputWrapper
from social_network_kata.printer_wrapper import PrinterWrapper
from social_network_kata.social_network_cli import SocialNetworkCLI
from social_network_kata.social_network_service import SocialNetworkService
from social_network_kata.input_parser import InputParser
from social_network_kata.command import Command
from social_network_kata.command_type import CommandType
from social_network_kata.post import Post

class TestCLI:
    def test_cli_can_add_post(self):
        user_name="PrincessAtta" 
        content="The caterpillar's using himself as live bait"
        mock_input = Mock(InputWrapper)
        mock_input.received_input.side_effect = [
            f"{user_name} -> {content}",
            "exit"
            ]
        mock_printer = Mock(PrinterWrapper)
        mock_social_network_service = Mock()
        mock_input_parser = Mock(InputParser)
        mock_input_parser.parse_user_input.side_effect = [
            Command(type=CommandType.POSTING, user_name=user_name, command_input=content),
            Command(type=CommandType.EXIT)
        ]
        social_network_cli = SocialNetworkCLI(
            social_network_service=mock_social_network_service, 
            printer=mock_printer,
            input=mock_input,
            input_parser=mock_input_parser)

        social_network_cli.run()
        
        mock_social_network_service.add_post.assert_called_once_with(user_name, content)

    def test_cli_can_get_posts_for_username(self):
        user_name="PrincessAtta" 
        content="The caterpillar's using himself as live bait"
        mock_input = Mock(InputWrapper)
        mock_input.received_input.side_effect = [
            user_name,
            "exit"
            ]
        mock_printer = Mock(PrinterWrapper)
        mock_social_network_service = Mock(SocialNetworkService)
        mock_input_parser = Mock(InputParser)
        mock_input_parser.parse_user_input.side_effect = [
            Command(type=CommandType.READING, user_name=user_name),
            Command(type=CommandType.EXIT)
        ]
        mock_social_network_service.get_posts_for_username.return_value = "The caterpillar's using himself as live bait (1 minute ago)"
        social_network_cli = SocialNetworkCLI(
            social_network_service=mock_social_network_service, 
            printer=mock_printer,
            input=mock_input,
            input_parser=mock_input_parser
        )

        social_network_cli.run()

        mock_printer.print.assert_called_once_with("The caterpillar's using himself as live bait (1 minute ago)")
        

