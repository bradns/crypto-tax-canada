import os
import click


@click.command()
@click.option('--datadir', help='The directory containing your transaction reports')
def process_csv(datadir):
    print("Processing CSV files found in: " + datadir)
    f_list = [os.path.join(datadir, f) for f in os.listdir(datadir)]
    print("Found " + str(len(f_list)) + " files to process")
    num_buy, num_sell = 0, 0
    for f in f_list:
        with open(f, 'r') as fin:
            header = fin.readline()
            for l in fin:
                fields = l.split(',')
                if fields[0] == 'buy':
                    num_buy += 1
                elif fields[0] == 'sell':
                    num_sell += 1
    print(f"Found a total of {num_buy} buy transactions and {num_sell} sell transactions") 


if __name__ == '__main__':
    process_csv()
