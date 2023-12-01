import os
import requests
from urllib.parse import urlsplit
from dotenv import load_dotenv

load_dotenv()


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
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_link.netloc+parsed_link.path}/clicks/summary"
    header = {"Authorization": f"Bearer {token}"}
    payload = {'unit': 'day', 'units': -1}
    response = requests.get(url, headers=header, params=payload)
    response.raise_for_status()
    clicks_count = response.json().get("total_clicks")
    return clicks_count


def is_bitlink(token, url):
    parsed_link = urlsplit(url)
    link_without_scheme = parsed_link.netloc+parsed_link.path
    api_url = f"https://api-ssl.bitly.com/v4/bitlinks/{link_without_scheme}"
    header = {"Authorization": f"Bearer {token}"}
    response = requests.get(api_url, headers=header)
    is_bitlink = response.ok
    return is_bitlink


def main(url=input("Введите ссылку: ")):
    try:
        request = requests.get(url)
        request.raise_for_status()
        token = os.getenv("BITLY_ACCESS_TOKEN", default=None)
        check_for_bitlink = is_bitlink(token, url)
        if check_for_bitlink is True:
            return print(count_clicks(token, url))
        return print(shorten_link(token, url))
    except requests.exceptions.HTTPError:
        print("Ошибка введенного url, проверьте корректность ссылки")


if __name__ == '__main__':
        main()