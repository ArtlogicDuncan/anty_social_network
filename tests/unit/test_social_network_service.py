from unittest.mock import Mock
from datetime import datetime

from social_network_kata.social_network_service import SocialNetworkService
from social_network_kata.clock_wrapper import ClockWrapper
from social_network_kata.post import Post
from social_network_kata.post_repository import PostRepository

class TestSocialNetworkService:

    def test_add_post(self):
        mock_clock = Mock(ClockWrapper)
        created_at = datetime(year=2024, month=11, day=1, hour=12, minute=0, second=0)
        mock_clock.get_time.return_value = created_at
        user_name="PrincessAtta" 
        content="The caterpillar's using himself as live bait"
        post = Post(
            user_name=user_name,
            content=content,
            created_at=created_at
        )
        mock_repository = Mock(PostRepository)
        social_network_service = SocialNetworkService(clock=mock_clock, repository=mock_repository)

        social_network_service.add_post(user_name=user_name, content=content)

        mock_repository.add_post.assert_called_once_with(post)

