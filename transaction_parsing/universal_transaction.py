from enum import Enum


class TransactionType(Enum):
    Buy = 1
    Sell = 2

class UniversalTransaction:
    def __init__(self, trans_type, datetime, major, minor, amount, rate):
        self.trans_type = trans_type
        self.datetime = datetime
        self.major = major
        self.minor = minor
        self.amount = amount
        self.rate = rate
