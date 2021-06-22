import hashlib

import requests

from config import Config


class RedirectByCurrency:
    def __init__(self):
        pass
    __all_currencies = {'USD': '840', 'RUB': '643', 'EUR': '978'}

    def pay(self, amount: float, currency: str, shop_order_id: int):
        method = "post"
        action = "https://pay.piastrix.com/ru/pay"

        request_dict = {
            "currency": self.__all_currencies[currency],
            "amount": '{0:.2f}'.format(amount),
            "shop_id": str(Config.shop_id),
            "shop_order_id": str(shop_order_id)
        }
        request_dict['sign'] = self._sign(request_dict, ['amount', 'currency', 'shop_id', 'shop_order_id'])

        return self._create_form(method, action, request_dict)

    def bill(self, amount: float, currency: str, shop_order_id: int):
        url = 'https://core.piastrix.com/bill/create'

        request_dict = {
            "payer_currency": self.__all_currencies[currency],
            "shop_amount": '{0:.2f}'.format(amount),
            "shop_currency": self.__all_currencies[currency],
            "shop_id": str(Config.shop_id),
            "shop_order_id": str(shop_order_id),
        }
        request_dict['sign'] = self._sign(request_dict,
                                          ['shop_amount', 'shop_currency', 'shop_id', 'shop_order_id',
                                           'payer_currency'])

        return self._post(url, request_dict)['url']

    def invoice(self, amount: float, currency: str, shop_order_id: int):
        url = 'https://core.piastrix.com/invoice/create'

        request_dict = {
            "currency": self.__all_currencies[currency],
            "amount": '{0:.2f}'.format(amount),
            "payway": 'advcash_rub',
            "shop_id": str(Config.shop_id),
            "shop_order_id": str(shop_order_id),
        }
        request_dict['sign'] = self._sign(request_dict, ['amount', 'currency', 'payway', 'shop_id', 'shop_order_id'])

        r_data = self._post(url, request_dict)

        return self._create_form(r_data["method"], r_data["url"], r_data['data'])

    @staticmethod
    def _sign(data, required_fields):
        sorted_data = [data[key] for key in sorted(required_fields)]
        signed_data = ':'.join(sorted_data) + Config.secret_key
        sign = hashlib.sha256(signed_data.encode('utf-8')).hexdigest()
        return sign

    @staticmethod
    def _create_form(method, action, request_dict):
        form = f'<form name="Pay" method="{method}" action="{action}" accept-charset="UTF-8"> '
        for item_request in request_dict:
            form += f'<input type="hidden" name="{item_request}" value="{request_dict[item_request]}"/> '
        form += f'<input type="submit" value="Оплатить"/></form>'

        return form

    @staticmethod
    def _post(url, request_dict):
        r = requests.post(url, json=request_dict)
        return r.json()['data']
