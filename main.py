from models import is_shorten_link, count_clicks, get_short_link
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    vk_token = os.environ['VK_TOKEN']
    
    parser = argparse.ArgumentParser(description='Управление ссылками VK.')
    parser.add_argument('url', type=str, help='Ссылка для сокращения или проверки переходов')

    args = parser.parse_args()
    url = args.url

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
