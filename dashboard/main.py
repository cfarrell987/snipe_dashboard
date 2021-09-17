import requests
import os
import json
import pwd

def get_logged_user():

    try:
        return os.getlogin()
    except:
        pass

    try:
        user = os.environ['USER']
    except KeyError:
        return getpass.getuser()

    if user == 'root':
        try:
            return os.environ['SUDO_USER']
        except KeyError:
            pass

        try:
            pkexec_uid = int(os.environ['PKEXEC_UID'])
            return pwd.getpwuid(pkexec_uid).pw_name
        except KeyError:
            pass
    return user

def get_home_path():
    home_dir = pwd.getpwnam(get_logged_user()).pw_dir
    return home_dir


# Define Settings needed for authenticating and sending a GET request. Will Change this later as querystring will be fairly specific to each GET request
def rest_settings(home):

    home_path = home
    api_key = str(home_path + "/Development/snipe_dashboard/resources/api_key.txt")

    with open(api_key, "r") as file:
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

    home_path = get_home_path()

    querystring, headers = rest_settings(home_path)
    print(headers)
    models = get_models("https://develop.snipeitapp.com/api/v1/hardware",
                        headers)
    hardware = get_hardware("https://develop.snipeitapp.com/api/v1/hardware",
                            querystring, headers)
    parser(models, hardware)
