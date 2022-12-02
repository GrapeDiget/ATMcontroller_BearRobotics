from enum import Enum, auto


class State(Enum):
    INIT = auto()
    MAIN = auto()
    ACCOUNT = auto()
    BALANCE = auto()
    DEPOSIT = auto()
    WITHDRAW = auto()
