import pyexcel

from transaction_parsing.universal_transaction import UniversalTransaction, TransactionType


def parse_xlsx(xlsx_filename):
    result = []
    records = pyexcel.iget_records(file_name=xlsx_filename)
    for r1 in list(records):
        tr_type = TransactionType.Buy if r1["Type"].lower() == "buy" else TransactionType.Sell
        ut = UniversalTransaction(tr_type, "0", "0", "0", "0", "0")
        result.append(ut)
    return result