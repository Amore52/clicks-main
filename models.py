import requests
from urllib.parse import urlsplit



def get_short_link(vk_token, url):
    vk_api_url = 'https://api.vk.com/method/utils.getShortLink'
    payload = {
        'access_token': vk_token,
        'v': '5.199',
        'url': url
    }

    response = requests.get(vk_api_url, params=payload)
    response.raise_for_status()
    api_response = response.json()
    return api_response['response']['short_url']



def count_clicks(vk_token, short_url):
    vk_api_url = 'https://api.vk.com/method/utils.getLinkStats'
    parsed_split = urlsplit(short_url)
    key_url_parsed = parsed_split.path.split('/')[-1]
    payload = {
        'access_token': vk_token,
        'v': '5.199',
        'key': key_url_parsed,
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
    return 'vk.cc' in url

def get_link_info(vk_token, url):
    if is_shorten_link(url) is True:
        clicks = count_clicks(vk_token, url)
        print('Количество переходов по ссылке:', clicks)

    else:
        short_url = get_short_link(vk_token, url)
        clicks = count_clicks(vk_token, short_url)
        print('Сокращенная ссылка:', short_url)
        print('Количество переходов по ней:', clicks)







