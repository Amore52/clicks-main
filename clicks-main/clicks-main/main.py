from urllib.parse import urlparse

import requests


def shorten_link(token, url):
    vk_url = 'https://api.vk.ru/method/utils.getShortLink'
    payload = {
        'access_token': token,
        'v': '5.199',
        'url': url
        }
    try:
        response = requests.get(vk_url, params=payload)
        response.raise_for_status()
        data = response.json()
        value1 =  data.get('response')
        short_url = value1.get('short_url')
        key_url = value1.get('key')
        return short_url, key_url
    except:
        print('Ошибка, неверный адрес')
    return None, None


def count_clicks(token):
    vk_url = 'https://api.vk.ru/method/utils.getLinkStats'

    try:
        payload = {
        'access_token': token,
        'v': '5.199',
        'key': short_key,
        'extended': '0'
        }
        response = requests.get(vk_url, params=payload)
        response.raise_for_status()
        data = response.json()
        return data['response']['stats']
    except:
        print('Ошибка, неверный ключ')
        return None


token = 'd70059fdd70059fdd70059fdb7d41feed4dd700d70059fdb1fe855c86567060d246adc4'
url = input('Введите ссылку: ')
short_url, short_key = shorten_link(token,url)
print(short_url)
print(count_clicks(token))









