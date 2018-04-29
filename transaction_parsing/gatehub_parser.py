import csv
from datetime import datetime

from transaction_parsing.universal_transaction import UniversalTransaction, TransactionType, Exchange
from transaction_parsing.historical_info import HistoricalInfo


def parse_gatehub(csv_filepath):
    result = []
    hinfo = HistoricalInfo()
    with open(csv_filepath, 'r') as fin:
        reader = csv.reader(fin, delimiter=',', quotechar='"')
        header_skipped = False
        exchange_lines = []
        trans_hashes = []
        for flds in reader:
            if header_skipped == False:
                header_skipped = True
                continue
            if flds[2] == "exchange":
                exchange_lines.append(flds)
                trans_hashes.append(flds[1])

        trans_hash_set = set(trans_hashes)
        assert len(exchange_lines) % 2 == 0

        for h in trans_hash_set:
            trans_lines = [flds for flds in exchange_lines if flds[1] == h]
            assert len(trans_lines) == 2
            flds1, flds2 = trans_lines[0], trans_lines[1]
            dt1 = datetime.strptime(flds1[0], "%b %d, %Y, %H:%M")
            dt2 = datetime.strptime(flds2[0], "%b %d, %Y, %H:%M")
            assert dt1.timestamp() == dt2.timestamp()
            quant1, currency1 = float(flds1[3]), flds1[4]
            quant2, currency2 = float(flds2[3]), flds2[4]
            if quant1 > 0:
                cad_rate = hinfo.get_cad_price(currency1, dt1)
                ut = UniversalTransaction(Exchange.GateHub, TransactionType.Buy, dt1, currency1, currency2, quant1, abs(quant2) / quant1, cad_rate)
            else:
                cad_rate = hinfo.get_cad_price(currency2, dt1)
                ut = UniversalTransaction(Exchange.GateHub, TransactionType.Buy, dt1, currency2, currency1, quant2, abs(quant1) / quant2, cad_rate)
            result.append(ut)
    return result
