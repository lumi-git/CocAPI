class distantSourceObject:
    def __init__(self,loadInfo:bool) -> None:
        self.global_info:dict = None
        if loadInfo:
            self.loadDistantInfos()

    def loadDistantInfos(self) -> None:
        pass

    def getInfos(self) -> dict:
        if self.global_info is None:
            self.loadDistantInfos()
        return self.global_info
    

def usesDistantInfos( func ):
    def wrapper(*args, **kwargs):
        if args[0].global_info is None:
            args[0].loadDistantInfos()
        return func(*args, **kwargs)
    return wrapper
