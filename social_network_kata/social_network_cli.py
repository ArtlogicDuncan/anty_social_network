from social_network_kata.input_wrapper import InputWrapper
from social_network_kata.printer_wrapper import PrinterWrapper
from social_network_kata.social_network_service import SocialNetworkService
from social_network_kata.input_parser import InputParser
from social_network_kata.command_type import CommandType
from social_network_kata.command import Command

class SocialNetworkCLI:
    def __init__(self, 
            social_network_service: SocialNetworkService, 
            printer: PrinterWrapper, 
            input: InputWrapper, 
            input_parser: InputParser):
        self.social_network_service = social_network_service
        self.printer = printer
        self.input = input
        self.input_parser = input_parser
        self.is_running = True

    def exit(self):
        self.is_running = False
    
    def run(self):
        while self.is_running:
            user_input = self.input.received_input()
            command: Command = self.input_parser.parse_user_input(user_input)
            match command.type:
                case CommandType.POSTING:
                    user_name = command.user_name
                    post_content = command.command_input
                    self.social_network_service.add_post(user_name, post_content)
                case CommandType.EXIT:
                    self.exit()
                case CommandType.READING:
                    self.social_network_service.get_posts_for_username(command.user_name)
                case _:
                    continue
