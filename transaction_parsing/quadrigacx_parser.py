from transaction_parsing.universal_transaction import UniversalTransaction, TransactionType


def parse_csv(csv_filepath):
    result = []
    with open(csv_filepath, 'r') as fin:
        for l in fin:
            flds = l.split(",")
            tr_type = TransactionType.Buy if flds[0].lower() == "buy" else TransactionType.Sell
            ut = UniversalTransaction(tr_type, flds[9], flds[1], flds[2], flds[3], flds[4])
            result.append(ut)
    return result
