from unittest.mock import patch, Mock

from social_network_kata.social_network_cli import SocialNetworkCLI
from social_network_kata.post import Post

class TestCLI:

    @patch('builtins.input', side_effect=["PrincessAtta -> The caterpillar's using himself as live bait"])
    def test_cli_calls_add_post(self, side_effect):
        post = Post(user_name="PrincessAtta", content="The caterpillar's using himself as live bait")
        mock_printer = Mock()
        mock_social_network_service = Mock()
        social_network_cli = SocialNetworkCLI(social_network_service=mock_social_network_service, printer=mock_printer)

        social_network_cli.run()
        
        mock_social_network_service.add_post.assert_called_once_with(post)