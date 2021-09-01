import requests
import os

def get(url):
    url = url
    response = requests.get(url)
    print(response.text)

def


if __name__ == '__main__':
    get("https://cdn.valhallahosting.ca/")
