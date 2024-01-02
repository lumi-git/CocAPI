import requests
from cocapi.requestsSettings import *

def verifyPlayerToken(playerTag:str, playerToken:str):
    response = requests.post(getVerifyPlayerTokenApiUrl(playerTag), headers=getAPIHeader(), json=getPlayerVerifyBody(playerToken))

    if response.json()["status"] == "ok":
        return True
    else:
        return False
