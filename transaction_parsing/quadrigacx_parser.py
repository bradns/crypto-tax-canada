from datetime import datetime

from transaction_parsing.universal_transaction import UniversalTransaction, TransactionType, Exchange


def parse_csv(csv_filepath):
    result = []
    with open(csv_filepath, 'r') as fin:
        header_skipped = False
        for l in fin:
            if header_skipped == False:
                header_skipped = True
                continue
            flds = l.split(",")
            tr_type = TransactionType.Buy if flds[0].lower() == "buy" else TransactionType.Sell
            dt_str = flds[8].split('.')[0] # Don't really need the milliseconds
            dt = datetime.utcfromtimestamp(float(dt_str))
            if flds[2].upper() == "CAD": # I don't need to handle non-CAD transactions, so I'll just throw an error for now
            	cad_rate = float(flds[4])
            else:
            	raise Exception("Unable to handle non-CAD transactions for the QuadrigaCX exchange")
            ut = UniversalTransaction(Exchange.Quadriga, tr_type, dt, flds[1].upper(), flds[2].upper(), float(flds[3]), float(flds[4]), cad_rate)
            result.append(ut)
    return result
