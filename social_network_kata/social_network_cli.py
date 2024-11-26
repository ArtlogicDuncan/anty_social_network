from social_network_kata.post import Post
from social_network_kata.input_wrapper import InputWrapper
from social_network_kata.printer_wrapper import PrinterWrapper
from social_network_kata.social_network_service import SocialNetworkService

class SocialNetworkCLI:
    def __init__(self, social_network_service: SocialNetworkService, printer: PrinterWrapper, input: InputWrapper):
        self.social_network_service = social_network_service
        self.printer = printer
        self.input = input
    
    def run(self):
        user_input = self.input.received_input()
        [user_name, post_content] = user_input.split(' -> ')
        new_post = Post(user_name=user_name, content=post_content)
        self.social_network_service.add_post(new_post)
            
        # switch
        # wait for input
        # pass input to input_processor
