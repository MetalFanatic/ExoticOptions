from typing import Union


class InvalidMertonModelInstantiation(Exception):
    """
    Custom error that raises when BlackScholes has merton set to True
    but q is null
    """

    def __init__(self, value: Union[int, float], message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class InvalidAction(Exception):
    """
    Custom error that raises when action is not between 0 and 1
    """

    def __init__(self, value: int, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)
