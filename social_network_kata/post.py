#from social_network_kata.user import User

class Post:
    ID = str

    def __init__(self, id: ID, content: str, user_id: str):
        self.id = id
        self.content = content
        self.user_id = user_id
        pass