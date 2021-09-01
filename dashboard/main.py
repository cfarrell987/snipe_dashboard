import requests
import os


def get(url):
    url = url
    response = requests.get(url)
    print(response.text)


if __name__ == '__main__':
    get("https://cdn.valhallahosting.ca/")
