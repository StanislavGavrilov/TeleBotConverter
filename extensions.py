import requests
import json
from config import keys


class APIExeption(Exception):
    pass
class CryptoConverter:
    @staticmethod
    def convert (qoute, base,amount):


        if qoute == base:
            raise APIExeption(f'Не возможно обработать одинаковые валюты. {base}')
        try:
            qoute_ticker = keys[qoute]
        except KeyError:
            raise APIExeption(f'Не удалось обработать валюту. {qoute}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIExeption(f'Не удалось обработать валюту. {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIExeption(f'Не удалось обработать количество. {amount}')

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={keys[qoute]}&tsyms={keys[base]}")
        total_base = json.loads(r.content)[keys[base]]
        return total_base
