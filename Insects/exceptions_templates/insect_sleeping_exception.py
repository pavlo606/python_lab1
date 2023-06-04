"""InsectSleepingException template"""

class InsectSleepingException(Exception):
    """Raised when the insect is already sleepeing and you try to make it sleep or vice versa"""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
