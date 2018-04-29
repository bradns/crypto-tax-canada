from enum import Enum


class Exchange(Enum):
    Quadriga = 1
    Binance = 2
    GateHub = 3

class TransactionType(Enum):
    Buy = 1
    Sell = 2

class UniversalTransaction:
    def __init__(self, exchange, trans_type, datetime, major, minor, amount, rate, cad_rate):
        self.exchange = exchange
        self.trans_type = trans_type
        self.datetime = datetime
        self.major = major
        self.minor = minor
        self.amount = amount
        self.rate = rate
        self.cad_rate = cad_rate

    def __str__(self):
    	ex_strs = {Exchange.Quadriga: "QCX", Exchange.Binance: "BIN", Exchange.GateHub: "GAT"}
    	type_strs = {TransactionType.Buy: "BUY ", TransactionType.Sell: "SELL"}
    	return f"{ex_strs[self.exchange]} {self.datetime} {type_strs[self.trans_type]}  {self.amount:.8f} {self.major}\tAT {self.rate:.8f} {self.minor}\t(CAD$ {self.cad_rate})"
