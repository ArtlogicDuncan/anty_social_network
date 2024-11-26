class InputWrapper:

    def __init__(self) -> None:
        pass

    def received_input(self) -> str:
        raise NotImplementedError("InputWrapper: received_input not implemented")