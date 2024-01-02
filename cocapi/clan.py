import cocapi.apiGetter as apiGetter
class Clan : 
    def __init__(self, clan_tag):
        self.clan_tag = clan_tag
        self.clan_info = self.getClanInfo()

    def getClanInfo(self) -> dict:
        return apiGetter.getClanInfo(self.clan_tag)
    
    def getMembers(self) -> list[dict]:
        return self.clan_info.get("memberList", [])
