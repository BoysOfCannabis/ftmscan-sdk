import aiohttp
import abc

class BlockExplorer(abc.ABC):
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
    
class FTMExplorer(BlockExplorer):
    def get_transactions(self):
        ...
        