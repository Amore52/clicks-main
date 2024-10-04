import requests
from urllib.parse import urlsplit
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('TOKEN')
url = input('Введите ссылку: ')

def short_link(TOKEN, url):
    vk_api_url = 'https://api.vk.com/method/utils.getShortLink'
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


def count_clicks(TOKEN, short_url):
    vk_api_url = 'https://api.vk.com/method/utils.getLinkStats'
    try:
        parsed_split = urlsplit(short_url)
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
    except IndexError:  # Новая ссылка без переходов.
        return '0'


def is_shorten_link(url):
    if 'vk.cc' in url:
        clicks = count_clicks(TOKEN, url)
        print('Количество переходов по ссылке:', clicks)
    else:
        short_url = short_link(TOKEN, url)
        clicks = count_clicks(TOKEN, short_url)
        print('Сокращенная ссылка:', short_url)
        print('Количество переходов по ней:', clicks)


if __name__ == "__main__":
    is_shorten_link(url)