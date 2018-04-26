import os
import click

from transaction_parsing.universal_transaction import TransactionType
from transaction_parsing.quadrigacx_parser import parse_csv
from transaction_parsing.binance_parser import parse_xlsx
from transaction_processing.transaction_processor import TransactionProcessor

@click.command()
@click.option('--datadir', help='The directory containing your transaction reports')
def process_csv(datadir):
    print("Processing files found in: " + datadir)
    f_list = [os.path.join(datadir, f) for f in os.listdir(datadir)]
    print("Found " + str(len(f_list)) + " files to process")
    num_buy, num_sell = 0, 0
    ut_list = []
    for f in f_list:
        if f.endswith(".csv"):
            ut_list.extend(parse_csv(f))
        elif f.endswith(".xlsx"):
            ut_list.extend(parse_xlsx(f))
    num_buy = len(list(filter(lambda i: i.trans_type == TransactionType.Buy, ut_list)))
    num_sell = len(list(filter(lambda i: i.trans_type == TransactionType.Sell, ut_list)))
    print(f"There are {num_buy} buy transactions and {num_sell} sell transactions")
    tp = TransactionProcessor()
    tp.process(ut_list)

if __name__ == '__main__':
    process_csv()
