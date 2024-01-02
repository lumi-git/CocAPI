class distantSourceObject:
    def __init__(self,loadInfo) -> None:
        self.global_info:dict = None
        if loadInfo:
            self.loadDistantInfos()

    def loadDistantInfos(self) -> None:
        pass

    def setInformationGetter(self, getter,getterArgs) -> None:
        self.getter = getter
        self.getterArgs = getterArgs


    def getInfos(self) -> dict:
        if self.global_info is None:
            self.loadDistantInfos()
        return self.global_info