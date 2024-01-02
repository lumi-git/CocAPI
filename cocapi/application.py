import requests
from cocapi.requestsSettings import getAPIHeader


def createSession():
    session = requests.Session()
    session.headers.update(getAPIHeader())
    return session

class application :
    session = None
    def createApplication() :
        application.session = createSession()

