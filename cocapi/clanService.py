from cocapi.player import Player
from cocapi.clan import Clan
from cocapi.utils import loadplayersThreaded
class clanService:

    def getMembersOfClan(self, clanTag, loadPlayersData=False) -> list[Player]:
        clan = Clan(clanTag)
        player_tags = [member.get("tag") for member in clan.getInfos().get("memberList", [])]
        if loadPlayersData :
            ## run thread 
            return loadplayersThreaded(player_tags)
        else :
            return [Player(tag, loadPlayersData) for tag in player_tags]