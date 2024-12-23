from unittest.mock import patch, Mock
from datetime import datetime

from social_network_kata.social_network_cli import SocialNetworkCLI
from social_network_kata.social_network_service import SocialNetworkService
from social_network_kata.printer_wrapper import PrinterWrapper
from social_network_kata.input_wrapper import InputWrapper
from social_network_kata.clock_wrapper import ClockWrapper
from social_network_kata.post_repository import PostRepository
from social_network_kata.input_parser import InputParser

class TestPostMessage:
    def test_user_can_post_and_receives_success_message(self):
        mock_input = Mock(InputWrapper)
        mock_clock = Mock(ClockWrapper)
        mock_clock.get_time.side_effect = [
            datetime(year=2024, month=11, day=1, hour=12, minute=0, second=0),
            datetime(year=2024, month=11, day=1, hour=12, minute=1, second=0)
            ]
        mock_input.received_input.side_effect = [
            "PrincessAtta -> The caterpillar's using himself as live bait",
            "PrincessAtta",
            "exit"
            ]
        post_repository = PostRepository()
        social_network_service = SocialNetworkService(
            clock=mock_clock,
            post_repository=post_repository)
        mock_printer = Mock(PrinterWrapper)
        input_parser = InputParser()
        social_network_cli = SocialNetworkCLI(
            social_network_service=social_network_service, 
            printer=mock_printer,
            input=mock_input,
            input_parser=input_parser)
        
        social_network_cli.run()
        
        mock_printer.print.assert_called_once_with(f"The caterpillar's using himself as live bait (1 minute ago)")
