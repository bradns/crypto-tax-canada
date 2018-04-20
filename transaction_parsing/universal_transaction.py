from enum import Enum


class Exchange(Enum):
    Quadriga = 1
    Binance = 2
    GateHub = 3

class TransactionType(Enum):
    Buy = 1
    Sell = 2

class UniversalTransaction:
    def __init__(self, exchange, trans_type, datetime, major, minor, amount, rate):
        self.exchange = exchange
        self.trans_type = trans_type
        self.datetime = datetime
        self.major = major
        self.minor = minor
        self.amount = amount
        self.rate = rate

    def __str__(self):
        return f"{self.exchange}\t{self.trans_type}\t{self.datetime}\t{self.major}\t{self.minor}\t{self.amount}\t{self.rate}"
