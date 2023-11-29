import os
import requests
from urllib.parse import urlsplit
from dotenv import load_dotenv

load_dotenv()

def shorten_link(link):
    try:
        token = os.getenv("ACCESS_TOKEN")
        url = "https://api-ssl.bitly.com/v4/bitlinks"
        header = {"Authorization": f"Bearer {token}"}
        payload = {"long_url": link}
        response = requests.post(url, headers=header, json=payload)
        response.raise_for_status()
        bitlink = response.json().get('link')
        return bitlink
    except requests.exceptions.HTTPError:
        print(f"Ошибка введенного url, проверьте корректность ссылки")


def count_clicks(link):
    try:
        parsed_link = urlsplit(link)
        token = os.getenv("ACCESS_TOKEN")
        url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_link.netloc+parsed_link.path}/clicks/summary?unit=day&units=-1"
        header = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=header)
        response.raise_for_status()
        clicks_count = response.json().get("total_clicks")
        return clicks_count
    except requests.exceptions.HTTPError:
        print(f"Ошибка введенного url, проверьте корректность ссылки")


def is_bitlink(url=input("Введите ссылку: ")):
    parsed_link = urlsplit(url)
    if parsed_link.scheme != "":
        link_without_scheme = parsed_link._replace(scheme="").geturl()[2:]
    else:
        link_without_scheme = url
    token = os.getenv("ACCESS_TOKEN")
    api_url = f"https://api-ssl.bitly.com/v4/bitlinks/{link_without_scheme}"
    header = {"Authorization": f"Bearer {token}"}
    response = requests.get(api_url, headers=header)
    response_status = response.ok
    if response_status is True:
        return count_clicks(url)
    return shorten_link(url)




if __name__=='__main__':
        print(is_bitlink())