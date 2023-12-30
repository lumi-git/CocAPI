import API.apiGetter as apiGetter
import API.apiPost as apiPost
from API.concepts.clan import Clan

class Player:
    def __init__(self, playerTag):
        self.playerTag = playerTag
        self.global_info:dict = self.getPlayerInfo()

    def getPlayerInfo(self) -> dict:
        return apiGetter.getPlayerInfo(self.playerTag)

    def getClan(self) -> Clan:
        clan_info = self.global_info.get("clan", {})
        clan_tag = clan_info.get("tag", "No Clan")
        return Clan(clan_tag)
    
    def verify(self, playerToken):
        return apiPost.verifyPlayerToken(self.playerTag, playerToken)