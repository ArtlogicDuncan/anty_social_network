from datetime import datetime

class ClockWrapper:

    def __init__(self) -> None:
        pass

    def get_time() -> datetime:
        raise NotImplementedError("ClockWrapper: get_time not implemented")