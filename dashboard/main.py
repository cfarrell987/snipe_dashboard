import requests
import os


def get(url):
    url = url

    with open("api_key.txt", "r") as file:
        api_key = file.read()

    querystring = {
        "limit": "2",
        "offset": "0",
        "sort": "model",
        "order": "desc"
    }
    headers = {
        "Accept": "application/json",
        "Authorization": api_key.rstrip("'\n\"")
    }

    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    print(headers)
    print(response.text)


if __name__ == '__main__':
    get("https://develop.snipeitapp.com/api/v1/hardware")
