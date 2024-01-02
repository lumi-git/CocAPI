import requests
from cocapi.requestsSettings import *

def getPlayerInfo(playerTag:str):
    response = requests.get(getPlayerApiUrl(playerTag), headers=getAPIHeader())
    if response.status_code == 200:

        player_info = response.json()
        return player_info

    else:
        print("Error, status code : ", response.status_code)

def getClanInfo(clanTag:str):
    response = requests.get(getClanApiUrl(clanTag), headers=getAPIHeader())

    if response.status_code == 200:

        clan_info = response.json()
        return clan_info

    else:
        print("Error, status code : ", response.status_code)

def getClanMembers(clanTag:str):
    clanInfo = getClanInfo(clanTag)
    clanMembers = clanInfo.get("memberList", [])
    return clanMembers