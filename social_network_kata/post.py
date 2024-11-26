from dataclasses import dataclass
from datetime import datetime

@dataclass
class Post:
    user_name: str
    content: str
    created_at: datetime