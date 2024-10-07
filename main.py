from models import get_link_info
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    vk_token = os.getenv('TOKEN')
    url = input('Введите ссылку: ')


try:
    get_link_info(vk_token, url)
except KeyError:
    print('Неверная ссылка')

