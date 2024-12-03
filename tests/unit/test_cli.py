from unittest.mock import patch, Mock

from social_network_kata.input_wrapper import InputWrapper
from social_network_kata.printer_wrapper import PrinterWrapper
from social_network_kata.social_network_cli import SocialNetworkCLI
from social_network_kata.social_network_service import SocialNetworkService
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
        social_network_cli = SocialNetworkCLI(
            social_network_service=mock_social_network_service, 
            printer=mock_printer,
            input=mock_input)

        social_network_cli.run()
        
        mock_social_network_service.add_post.assert_called_once_with(user_name, content)

    def test_cli_can_get_posts_for_username(self):
        user_name="PrincessAtta" 
        content="The caterpillar's using himself as live bait"
        mock_input = Mock(InputWrapper)
        mock_input.received_input.side_effect = [
            f"{user_name} -> {content}",
            user_name,
            "exit"
            ]
        mock_printer = Mock(PrinterWrapper)
        mock_social_network_service = Mock(SocialNetworkService)
        social_network_cli = SocialNetworkCLI(
            social_network_service=mock_social_network_service, 
            printer=mock_printer,
            input=mock_input)

        social_network_cli.run()
        
        mock_social_network_service.get_posts_for_username.assert_called_once_with(user_name)

