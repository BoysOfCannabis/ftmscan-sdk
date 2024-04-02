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
        url = (
            self.API_URL
            + f"?module={request_payload['module']}&action={request_payload['action']}&address={request_payload['address']}&apikey={self.API_KEY}"
        )

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
