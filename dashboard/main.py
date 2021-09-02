import requests
import os
import json


# Define Settings needed for authenticating and sending a GET request. Will Change this later as querystring will be fairly specific to each GET request
def rest_settings():
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


# Sends GET request for models
def get_models(url, headers):
    url = url
    querystring = {
        "limit": "50",
        "offset": "0",
        "sort": "created_at",
        "order": "asc"
    }
    headers = headers

    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    return response.json()


# Sends GET request for hardware
def get_hardware(url, querystring, headers):
    url = url
    querystring = querystring
    headers = headers
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)

    return response.json()


def parser(models, hardware):
    hardware = hardware
    models = models
    json_models = "models.json"
    json_hardware = "hardware.json"
    curr_path = os.path.dirname(os.path.realpath(__file__))
    print("Writing to json")
    if os.path.exists(os.path.join(curr_path, json_models)):
        os.remove(os.path.join(curr_path, json_models))
        print("Deleted old json")

    with open(json_models, "w") as file:
        json.dump(models, file)

    if os.path.exists(os.path.join(curr_path, json_hardware)):
        os.remove(os.path.join(curr_path, json_hardware))
        print("Deleted old json")

    with open(json_hardware, "w") as file:
        json.dump(hardware, file)


#    print(json.dumps(models, indent=3))
#    print(json.dumps(hardware, indent=4))

if __name__ == '__main__':
    querystring, headers = rest_settings()
    models = get_models("https://develop.snipeitapp.com/api/v1/hardware",
                        headers)
    hardware = get_hardware("https://develop.snipeitapp.com/api/v1/hardware",
                            querystring, headers)
    parser(models, hardware)
