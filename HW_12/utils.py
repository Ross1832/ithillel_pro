import requests


def crypto_rate(currency):
    response = requests.get("https://bitpay.com/api/rates")
    data = response.json()
    temp = None
    for i in data:
        if i['code'].lower() == currency.lower():
            temp = i['rate']
    return temp
