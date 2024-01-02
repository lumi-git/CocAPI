from cocapi.player import Player
from cocapi.clan import Clan
class playerService:
    def getClanOfPlayer(self, player:Player, loadPlayersData=False) -> Clan:
        return Clan(player.getClanTag())
    
