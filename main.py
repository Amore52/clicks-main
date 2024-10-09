from models import is_shorten_link, count_clicks, get_short_link
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    vk_token = os.environ['TOKEN']
    url = input('Введите ссылку: ')

    try:
        if is_shorten_link(url) is True:
            clicks = count_clicks(vk_token, url)
            print('Количество переходов по ссылке:', clicks)

        else:
            print('Короткая ссылка: ', get_short_link(vk_token, url))
            print('Количество переходов по ссылке:', count_clicks(vk_token, url))
    except KeyError:
        print('Неверная ссылка')

if __name__ == "__main__":
    main()
