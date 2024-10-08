import requests
from urllib.parse import urlsplit



def get_short_link(vk_token, url):
    if is_shorten_link(url):
        return url
    vk_api_url = 'https://api.vk.com/method/utils.getShortLink'
    payload = {
        'access_token': vk_token,
        'v': '5.199',
        'url': url
    }

    response = requests.get(vk_api_url, params=payload)
    response.raise_for_status()
    api_response = response.json()
    return api_response['response'].get('short_url')


def count_clicks(vk_token, url):
    vk_api_url = 'https://api.vk.com/method/utils.getLinkStats'
    short_link = urlsplit(get_short_link(vk_token,url))
    key_short_link = short_link.path.split('/')[-1]
    payload = {
        'access_token': vk_token,
        'v': '5.199',
        'key': key_short_link,
        'interval': 'forever',
        'extended': 0
    }
    response = requests.get(vk_api_url, params=payload)
    response.raise_for_status()
    api_response = response.json()
    url_stats = api_response.get('response', {}).get('stats', [])
    url_views = url_stats[0].get('views', 0) if url_stats else 0
    return url_views


def is_shorten_link(url):
    split_url = urlsplit(url)
    return 'vk.cc' in split_url.netloc












