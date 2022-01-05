import json
import requests
from config import exchanges


class APIExeption(Exception):
    pass


class Converter:

    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIExeption(f'Не удалось обработать валюту {base}')
        try:
            quote_key = exchanges[quote.lower()]
        except KeyError:
            raise APIExeption(f'Не удалось обработать валюту {quote}')
        if base_key == quote_key:
            raise APIExeption(f'Невозможно перевести одинаковые ввалюты {base}.')
        try:
            amount = float(amount)
        except ValueError:
            raise APIExeption(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_key}&tsyms={quote_key}')
        resp = json.loads(r.content)
        new_price = resp[quote_key]*amount
        message = f'Стоимость {amount} {base} в {quote} составляет {new_price}.'
        return message
