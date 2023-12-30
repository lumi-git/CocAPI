import requests

# Constants
API_TOKEN = open("TOKEN",'r').read()
PLAYER_TAG = "#VPJY8CVG"
API_URL = f"https://api.clashofclans.com/v1/players/%23{PLAYER_TAG.replace('#', '')}"

# Headers for API request
headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Accept': 'application/json'
}

def get_building_levels():
    response = requests.get(API_URL, headers=headers)
    
    if response.status_code == 200:
        
        player_info = response.json()
        print(player_info)
        buildings = player_info.get('buildings', [])
        for building in buildings:
            print(f"Building: {building['name']}, Level: {building['level']}")
    else:
        print("Failed to fetch data:", response.status_code, response.text)

if __name__ == "__main__":
    get_building_levels()
