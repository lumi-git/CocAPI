# Create a new file named TOKEN and add your token into it.
# To get yourself a token, go at : https://developer.clashofclans.com/, register and create a token.
API_TOKEN = open("API/TOKEN",'r').readlines()[0].strip()


# Headers for API request
headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Accept': 'application/json'
}


def getPlayerVerifyBody(playerToken:str) -> dict:
    return  {"token": str(playerToken)}
    

def getPlayerApiUrl(PLAYER_TAG) -> str:
    return f"https://api.clashofclans.com/v1/players/%23{PLAYER_TAG.replace('#', '')}"

def getClanApiUrl(CLANTAG) -> str:
    return f"https://api.clashofclans.com/v1/clans/%23{CLANTAG.replace('#', '')}"

def getVerifyPlayerTokenApiUrl(PLAYER_TAG) -> str:
    return f"https://api.clashofclans.com/v1/players/%23{PLAYER_TAG.replace('#', '')}/verifytoken"