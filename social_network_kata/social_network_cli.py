from social_network_kata.input_wrapper import InputWrapper
from social_network_kata.printer_wrapper import PrinterWrapper
from social_network_kata.social_network_service import SocialNetworkService
from social_network_kata.input_parser import InputParser

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
    
    def run(self):
        while True:
            user_input = self.input.received_input()
            # parse command
            # switch user_input
            command = self.input_parser.parse_user_input(user_input)
            if user_input == "exit":
                # is exiting
                break
            elif command.type == "posting":
                [user_name, post_content] = user_input.split(' -> ')
                self.social_network_service.add_post(user_name, post_content)
            
        #is exited
