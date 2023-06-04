class InvalidModeError(Exception):
    """Raised when mode is incorrect"""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
