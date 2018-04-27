from datetime import datetime

from transaction_parsing.universal_transaction import UniversalTransaction, TransactionType, Exchange


def parse_gatehub(csv_filepath):
    result = []
    with open(csv_filepath, 'r') as fin:
        header_skipped = False
        exchange_lines = []
        trans_hashes = []
        for l in fin:
            if header_skipped == False:
                header_skipped = True
                continue
            flds = l.split(",")
            if flds[2] == "exchange":
                exchange_lines.append(l)
                trans_hashes.append(flds[1])

        trans_hash_set = set(trans_hashes)
        assert len(exchange_lines) % 2 == 0

        for h in trans_hash_set:
            trans_lines = exchange_lines.filter(lambda l: l.split(",")[1] == h)
            assert len(trans_lines) == 2
            flds1, flds2 = trans_lines[0].split(","), trans_lines[1].split(",")
            dt1 = datetime.strptime(flds1[0][1:-1], "%b %d, %Y, %H:%M")
            dt2 = datetime.strptime(flds2[0][1:-1], "%b %d, %Y, %H:%M")
            assert dt1.timestamp() == dt2.timestamp()
            quant1, currency1 = float(flds1[3]), flds1[4]
            quant2, currency2 = float(flds2[3]), flds2[4]
            if quant1 > 0:
                ut = UniversalTransaction(Exchange.GateHub, Transaction.Buy, dt1, currency1, abs(currency2), quant1, quant2 / quant1, 0)
            else:
                ut = UniversalTransaction(Exchange.GateHub, Transaction.Buy, dt1, currency2, abs(currency1), quant2, quant1 / quant2, 0)
            result.append(ut)
    return result
