from social_network_kata.interface import Interface
from social_network_kata.printer import Printer


class TestPostMessage:
    """"
    > Alice -> I love the weather today
    Alice can publish messages to a personal timeline.
    > Bob -> Damn! We lost!
    > Bob -> Good game though.
    """
    def test_user_can_post_and_receives_success_message(self):        
        printer = Printer()
        interface = Interface(printer = printer)
        user = "Atta" # Alice
        post_contents = "The caterpillar's using himself as live bait"
        command = Command(f'{user} -> {post_contents}')
        
        interface.send_command(command)
        
        printer.print.assert_called_once_with(f'Succesfully posted: {post_contents}')
