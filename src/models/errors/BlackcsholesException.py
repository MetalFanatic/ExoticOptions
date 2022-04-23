from typing import Union

class BlackSholesException(Exception):
    """
    Custom error that raises when BlackScholes has merton set to True
    but q is null
    """

    def __init__(self, value: Union[int, float] , message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)