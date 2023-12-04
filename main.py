import os
from urllib.parse import urlsplit
import argparse

import requests
from dotenv import load_dotenv


def shorten_link(token, link):
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    header = {"Authorization": f"Bearer {token}"}
    payload = {"long_url": link}
    response = requests.post(url, headers=header, json=payload)
    response.raise_for_status()
    bitlink = response.json().get('link')
    return bitlink


def count_clicks(token, link):
    parsed_link = urlsplit(link)
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_link.netloc}{parsed_link.path}/clicks/summary"
    header = {"Authorization": f"Bearer {token}"}
    payload = {'unit': 'day', 'units': -1}
    response = requests.get(url, headers=header, params=payload)
    response.raise_for_status()
    clicks_count = response.json().get("total_clicks")
    return clicks_count


def is_bitlink(token, url):
    parsed_link = urlsplit(url)
    link_without_scheme = f"{parsed_link.netloc}{parsed_link.path}"
    api_url = f"https://api-ssl.bitly.com/v4/bitlinks/{link_without_scheme}"
    header = {"Authorization": f"Bearer {token}"}
    response = requests.get(api_url, headers=header)
    return response.ok


def main(url):
    load_dotenv()
    try:
        token = os.environ["BITLY_ACCESS_TOKEN"]
        if is_bitlink(token, url):
            print("Количество переходов по ссылке битли: ", count_clicks(token, url))
        else:
            print(shorten_link(token, url))
    except requests.exceptions.HTTPError:
        print("Ошибка введенного url, проверьте корректность ссылки")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("link", help='Для преобразования введите ссылку')
    args = parser.parse_args()
    main(args.link)