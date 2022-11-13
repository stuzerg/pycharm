import requests
import json
from cfg import *

class APIexception(Exception):
    pass


class Mfn:

    @staticmethod
    def get_price(base, quote, amount):
        pair = values_dict[base] + values_dict[quote] # по текущему формату api сайта currate.ru,
                                                      # надо отправлять склееный тикет валют
                                                      # например USDEUR  RUBUSD
        r = requests.get(
            f'https://currate.ru/api/?get=rates&pairs={pair},&key={APIKEY}').content
        return '%.2f' % (float((json.loads(r))['data'][pair]) * amount) # результат оставляем до сотых долей
