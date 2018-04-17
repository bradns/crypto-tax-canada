import pyexcel

from transaction_parsing.universal_transaction import UniversalTransaction, TransactionType

MARKETS = {"BNBETH": ("BNB", "ETH"), "BCCETH": ("BCC", "ETH"), "IOTAETH": ("IOTA", "ETH"),
           "IOTABNB": ("IOTA", "BNB"), "VENETH": ("VEN", "ETH"), "ENGETH": ("ENG", "ETH")}


def parse_xlsx(xlsx_filename):
    result = []
    records = pyexcel.iget_records(file_name=xlsx_filename)
    for r1 in list(records):
        tr_type = TransactionType.Buy if r1["Type"].lower() == "buy" else TransactionType.Sell
        major, minor = MARKETS[r1["Market"]]
        ut = UniversalTransaction(tr_type, r1["Date"], major, minor, r1["Amount"], r1["Price"])
        result.append(ut)
    return result