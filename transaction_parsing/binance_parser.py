import pyexcel
from datetime import datetime

from transaction_parsing.universal_transaction import UniversalTransaction, TransactionType, Exchange
from transaction_parsing.historical_info import HistoricalInfo

MARKETS = {"BNBETH": ("BNB", "ETH"), "BCCETH": ("BCC", "ETH"), "IOTAETH": ("IOTA", "ETH"),
           "IOTABNB": ("IOTA", "BNB"), "VENETH": ("VEN", "ETH"), "ENGETH": ("ENG", "ETH")}


def parse_xlsx(xlsx_filename):
    result = []
    hinfo = HistoricalInfo()
    records = pyexcel.iget_records(file_name=xlsx_filename)
    for r1 in list(records):
        tr_type = TransactionType.Buy if r1["Type"].lower() == "buy" else TransactionType.Sell
        major, minor = MARKETS[r1["Market"]]
        dt = datetime.strptime(r1["Date"], "%Y-%m-%d %H:%M:%S")
        cad_rate = hinfo.get_cad_price(major, dt)
        ut = UniversalTransaction(Exchange.Binance, tr_type, dt, major, minor, float(r1["Amount"]), float(r1["Price"]), cad_rate)
        result.append(ut)
    return result
