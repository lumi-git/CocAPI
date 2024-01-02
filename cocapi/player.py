import cocapi.apiGetter as apiGetter
import cocapi.apiPost as apiPost
from cocapi.distantSourceObject import distantSourceObject,usesDistantInfos


class Player(distantSourceObject):
    def __init__(self, playerTag:str,loadInfo=True):
        self.playerTag = playerTag
        super().__init__(loadInfo)

    def loadDistantInfos(self) -> dict:
        self.global_info = apiGetter.getPlayerInfo(self.playerTag)

    @usesDistantInfos
    def getClanTag(self) -> str:
        clan_info = self.global_info.get("clan", {})
        clan_tag = clan_info.get("tag", "No Clan")
        return clan_tag
    
    def verify(self, playerToken):
        return apiPost.verifyPlayerToken(self.playerTag, playerToken)
    