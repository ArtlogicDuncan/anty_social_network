from enum import Enum

class CommandType(Enum):
    POSTING = "posting"
    READING = "reading"
    FOLLOWING = "following"
    WALL = "wall"
    EXIT = "exit"