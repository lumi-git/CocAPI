import requests
from API.requestsSettings import *

def verifyPlayerToken(playerTag, playerToken):
    response = requests.post(getVerifyPlayerTokenApiUrl(playerTag), headers=headers, json=getPlayerVerifyBody(playerToken))
    print(response.request.body)

    if response.json()["status"] == "ok":
        return True
    else:
        return False
