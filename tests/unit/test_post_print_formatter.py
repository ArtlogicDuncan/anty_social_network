from social_network_kata.post import Post
from social_network_kata.clock_wrapper import ClockWrapper

from unittest.mock import Mock
from datetime import datetime

class TestPostPrintFormatter:

    def test_single_post_is_formatted(self):
        mock_clock = Mock(ClockWrapper)
        created_at = datetime(year=2024, month=11, day=1, hour=12, minute=0, second=0)
        mock_clock.get_time.side_effect = [
            created_at,
            datetime(year=2024, month=11, day=1, hour=12, minute=1, second=0),
        ]
        post = Post(
            user_name="Slim",
            content="I'm the only stick with eyeballs!",
            created_at=datetime(year=2024, month=11, day=1, hour=12, minute=0, second=0)
        )
        post_formatter = PostFormatter(clock=mock_clock)

        formatted_post = post_formatter.format_post(post)

        assert formatted_post == "I'm the only stick with eyeballs! (1 minute ago)"