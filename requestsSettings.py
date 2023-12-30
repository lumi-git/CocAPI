# Create a new file named TOKEN and add your token into it.
# To get yourself a token, go at : https://developer.clashofclans.com/, register and create a token.
API_TOKEN = open("TOKEN",'r').read()


# Headers for API request
headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Accept': 'application/json'
}

def getPlayerApiUrl(PLAYER_TAG):
    return f"https://api.clashofclans.com/v1/players/%23{PLAYER_TAG.replace('#', '')}"
