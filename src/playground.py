from API.concepts.player import Player

def playground():
    game_api_token = "42xcd9xz" # this can be found in the game settings
    player = Player("#VPJY8CVG") # tag of player luminawight
    if player.verify(game_api_token) :
        print("Player verified " + player.global_info.get("name", "No Name"))

        members = player.getClan().getMembers()
        playerlist = []

        for member in members:
            playerlist.append( member.get("tag"))

        print(playerlist)