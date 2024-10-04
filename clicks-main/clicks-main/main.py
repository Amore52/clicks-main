from urllib.parse import urlparse, urlsplit

import requests

token = 'd70059fdd70059fdd70059fdb7d41feed4dd700d70059fdb1fe855c86567060d246adc4'
url = input('Введите ссылку: ')

def shorten_link(token, url):
    vk_url = 'https://api.vk.ru/method/utils.getShortLink'
    try:
        payload = {
            'access_token': token,
            'v': '5.199',
            'url': url
            }

        response = requests.get(vk_url, params=payload)
        response.raise_for_status()
        data = response.json()
        return data['response']['short_url']
    except KeyError:
        return 'Неверная ссылка'

def count_clicks(token):
    vk_url = 'https://api.vk.ru/method/utils.getLinkStats'

    try:
        parsed_split = urlsplit(shorten_link(token, url))
        key_parsed = parsed_split.path.split('/')[-1]
        payload = {
            'access_token': token,
            'v': '5.199',
            'key': key_parsed,
            'interval': 'forever',
            'extended': 0
        }
        response = requests.get(vk_url, params=payload)
        response.raise_for_status()
        data = response.json()
        views = data['response']['stats'][0]['views']
        return views
    except KeyError:
        return 'Ошибка сокращенной ссылки'


print(shorten_link(token,url))
print('Количество переходов по ссылке: ', count_clicks(token))
















