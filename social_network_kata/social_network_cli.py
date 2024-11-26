from social_network_kata.input_wrapper import InputWrapper
from social_network_kata.printer import Printer
from social_network_kata.social_network_service import SocialNetworkService

class SocialNetworkCLI:
    def __init__(self, social_network_service: SocialNetworkService, printer: Printer, input: InputWrapper):
        self.social_network_service = social_network_service
        self.printer = printer
        self.input = input
    
    def run(self):
        raise NotImplementedError