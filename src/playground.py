from API.concepts.player import Player

def playground():
    player = Player("#VPJY8CVG")
    members = player.getClan().getMembers()
    playerlist = []

    for member in members:
        playerlist.append( member.get("name"))

    print(playerlist)