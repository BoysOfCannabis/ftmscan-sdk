import aiohttp
import abc
from typing import List, Optional

Address = str
class BlockExplorer(abc.ABC):
    def __init__(self, API_KEY, API_URL):
        self.API_KEY = API_KEY
        self.API_URL = API_URL
        
    def send_request(self, request_payload):
        """Return a response"""
        
    
class FTMExplorer(BlockExplorer):
    def get_transactions(self, address: Address, token: Optional[str]):
        """
            Return a list of transactions as dict
            https://docs.ftmscan.com/api-endpoints/accounts
            
            set token none will return all transactions
            
            for example:
            {
                'in': 'Address',
                'out': 'Address',
                'amount': '',
                'token': '',
                'usd_value': '',
            }
        """
    
    def get_balance(self, address: Address | List[Address])-> float | List[float]:
        """Returns the balance of one or multiple fantom wallet
        https://docs.ftmscan.com/api-endpoints/accounts
        
        input like: "0x1B5248B881762576d630246feeA92E5c6FceD2e1"
        
        output like: 23.52
        """
        