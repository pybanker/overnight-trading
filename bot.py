# Imports
import ibapi
from ibapi.client import EClient
from ibapi.wrapper import EWrapper

# Variables
class IBApi(EWrapper,EClient):
    def __init__(self):
        EClient().__init__(self,self)

# Classes
class Bot:
    ib = None
    def __init__(self):
        ib = IBApi
        ib.connect('localhost','port','1')
        ib.run()


# Bot
bot = Bot()
