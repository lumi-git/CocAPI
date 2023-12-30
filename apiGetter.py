import requests
from requestsSettings import *

def getPlayerInfo(playerTag ):
    response = requests.get(getPlayerApiUrl(playerTag), headers=headers)

    if response.status_code == 200:

        player_info = response.json()
        return player_info

    else:
        print("Error, status code : ", response.status_code)
