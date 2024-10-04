import requests
from urllib.parse import urlsplit


TOKEN = 'd70059fdd70059fdd70059fdb7d41feed4dd700d70059fdb1fe855c86567060d246adc4'
url = input('Введите ссылку: ')

def short_link(TOKEN, url):
    vk_api_url = 'https://api.vk.ru/method/utils.getShortLink'
    try:
        payload = {
            'access_token': TOKEN,
            'v': '5.199',
            'url': url
            }

        response = requests.get(vk_api_url, params=payload)
        response.raise_for_status()
        data = response.json()
        return data['response']['short_url']
    except KeyError:
        return 'Неверная ссылка'

def count_clicks(TOKEN):
    vk_api_url = 'https://api.vk.ru/method/utils.getLinkStats'
    try:
        parsed_split = urlsplit(short_link(TOKEN, url))
        key_url_parsed = parsed_split.path.split('/')[-1]
        payload = {
            'access_token': TOKEN,
            'v': '5.199',
            'key': key_url_parsed,
            'interval': 'forever',
            'extended': 0
        }
        response = requests.get(vk_api_url, params=payload)
        response.raise_for_status()
        data = response.json()
        views_url = data['response']['stats'][0]['views']
        return views_url
    except KeyError:
        return 'Ошибка сокращенной ссылки'
    except IndexError: # Новая ссылка без переходов.
        return '0'


print('Сокращенная ссылка:', short_link(TOKEN,url))
print('Количество переходов по ссылке:', count_clicks(TOKEN))













