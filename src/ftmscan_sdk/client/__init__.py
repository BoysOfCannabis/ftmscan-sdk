import abc

import aiohttp

class BaseBlockExplorerClient(abc.ABC):
    def __init__(self, API_KEY, API_URL):
        self.API_KEY = API_KEY
        self.API_URL = API_URL

    @abc.abstractmethod
    def send_request(self, request_payload):
        """Return a response"""


class FTMExplorerClient(BaseBlockExplorerClient):

    def __init__(self, API_KEY):
        API_URL = "https://api.ftmscan.com/api"
        super().__init__(API_KEY, API_URL)

    async def send_request(self, request_payload):
        request_payload["apikey"] = self.API_KEY
        async with aiohttp.ClientSession() as session:
            async with session.get(self.API_URL, params=request_payload) as response:
                return await response.json()

