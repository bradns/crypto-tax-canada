from transaction_parsing.universal_transaction import UniversalTransaction, TransactionType


class TransactionError(Exception):
    pass

class TransactionProcessor:
    def __init__(self):
        self.state = {}

    def process(self, tlist):
        # Ensure that the transaction list is sorted
        tlist_sorted = sorted(tlist, key = lambda x: x.datetime)

        for t in tlist_sorted:
            if t.trans_type == TransactionType.Buy:
                if t.major not in self.state:
                    print(f"{t.datetime} BUY  {t.amount} {t.major} AT {t.rate} {t.minor} IN FIRST PURCHASE (ACB: {t.rate * t.amount})")
                    self.state[t.major] = (t.amount, t.rate * t.amount)
                else:
                    (last_amount, last_acb) = self.state[t.major]
                    cur_amount = last_amount + t.amount
                    cur_acb = last_acb + (t.rate * t.amount)
                    self.state[t.major] = (cur_amount, cur_acb)
                    print(f"{t.datetime} BUY  {t.amount} {t.major} AT {t.rate} {t.minor}  ===>  HOLDING {cur_amount} (ACB: {cur_acb})")
            elif t.trans_type == TransactionType.Sell:
                if t.major not in self.state:
                    #raise TransactionError(f"ERROR: No units of currency {t.major} have been bought.")
                    print(f"{t.datetime} SELL {t.amount} {t.major} at {t.rate} {t.minor}  ===>  NONE BOUGHT!")
                else:
                    (last_amount, last_acb) = self.state[t.major]
                    cur_amount = last_amount - t.amount
                    cur_acb = last_acb * ((last_amount - t.amount) / last_amount)
                    self.state[t.major] = (cur_amount, cur_acb)
                    print(f"{t.datetime} SELL {t.amount} {t.major} at {t.rate} {t.minor}  ===>  HOLDING {cur_amount} (ACB: {cur_acb})")
