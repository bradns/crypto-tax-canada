import os, pickle
import requests

CACHE_PKL = "price_cache.pkl"
CRYPTOCOMPARE_URL = "https://min-api.cryptocompare.com/data/"


class HistoricalInfo:
    def __init__(self):
        self.cached_prices = {}
        if os.path.exists(CACHE_PKL) and os.path.isfile(CACHE_PKL):
            with open(CACHE_PKL, 'rb') as fin:
                self.cached_prices = pickle.load(fin)

    def get_cad_price(self, symbol, dt):
        if (symbol, dt) in self.cached_prices:
            return self.cached_prices[(symbol, dt)]
        else:
            p = self.get_cad_price_webapi(symbol, dt)
            self.cached_prices[(symbol, dt)] = p
            with open(CACHE_PKL, 'wb') as fout:
                pickle.dump(self.cached_prices, fout)
            return p

    def get_cad_price_webapi(self, symbol, dt):
        api_symbol = symbol if symbol != 'IOTA' else 'IOT' # This API seems to require prices for IOTA to be checked with IOT...
        api_symbol = api_symbol if symbol != 'BCC' else 'BCH' # A difference between the symbols used by binance and the API
        ts = int(dt.timestamp())
        params = {'fsym': api_symbol, 'tsym': 'CAD', 'toTs': str(ts)}
        r = requests.get(CRYPTOCOMPARE_URL + "histohour", params=params)
        if r.status_code != 200:
            raise Exception(f"ERROR: Unable to retrieve a price from the web-api: {r}")
        else:
            json = r.json()
            return json['Data'][0]['low']
