from social_network_kata.command_type import CommandType
from dataclasses import dataclass
from typing import Optional

@dataclass
class Command:
    type: CommandType
    user_name: Optional[str] = None
    command_input: Optional[str] = None