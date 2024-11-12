from social_network_kata.command import Command
from social_network_kata.interface import Interface
from social_network_kata.printer import Printer

ALICE = "PrincessAtta"
ALICE_POST = "The caterpillar's using himself as live bait"
BOB = "Slim"
BOB_POST = "I'm the only stick with eyeballs!"
CHARLIE = "Heimlich"
CHARLIE_POST = "Someday, I will be a beautiful butterfly, and then everything will be better." 

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
        user = ALICE
        post_contents = ALICE_POST
        command = f'{user} -> {post_contents}'

        terminal.call(
            "AntySocialNetwork()", # Anty: post something.
            f"{command}"
        )

        subprocess.getoutput() # something like this to input text to terminal
        
        printer.print.assert_called_once_with(f'Succesfully posted: {post_contents}')
