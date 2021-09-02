import requests
import os
import json


def settings():
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

    return querystring, headers


def get_model(url):
    url = url


def get_hardware(url, querystring, headers):
    url = url
    querystring = querystring
    headers = headers
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)

    return response.json()


def parser(response):
    response = response
    print(json.dumps(response, indent=4))


if __name__ == '__main__':
    querystring, headers = settings()
    hardware = get_hardware("https://develop.snipeitapp.com/api/v1/hardware",
                            querystring, headers)
    parser(hardware)
