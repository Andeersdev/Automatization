from enum import Enum

class Message(str, Enum):
    SUCCESS_MESSAGE = 'Process Success.'

    def __str__(self):
        return self.value