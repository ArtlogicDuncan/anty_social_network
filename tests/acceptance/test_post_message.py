from unittest.mock import patch, Mock

from social_network_kata.social_network_cli import SocialNetworkCLI
from social_network_kata.social_network_service import SocialNetworkService
from social_network_kata.printer import Printer

ALICE = "PrincessAtta"
ALICE_POST = "The caterpillar's using himself as live bait"
BOB = "Slim"
BOB_POST = "I'm the only stick with eyeballs!"
CHARLIE = "Heimlich"
CHARLIE_POST = "Someday, I will be a beautiful butterfly, and then everything will be better." 

class TestPostMessage:
    @patch('builtins.input', side_effect=["PrincessAtta -> The caterpillar's using himself as live bait"])
    def test_user_can_post_and_receives_success_message(self, side_effect):
        social_network_service = SocialNetworkService()
        mock_printer = Mock(Printer)
        social_network_cli = SocialNetworkCLI(social_network_service=social_network_service, printer=mock_printer)
        
        social_network_cli.run()
        
        mock_printer.print.assert_called_once_with(f"Succesfully posted: PrincessAtta -> The caterpillar's using himself as live bait")
