from typing import Dict, List

from client import FTMExplorerClient
from utils import logger as logging

from .account_typing import GetFtmBalanceAddressInterface


class Account(FTMExplorerClient):

    async def get_ftm_balance_for_single_address(self, address: str) -> Dict:

        logging.info(f"try to get ftm balance for {address}")
        request_payload: GetFtmBalanceAddressInterface = {
            "module": "account",
            "action": "balance",
            "address": address,
        }
        response = await self.send_request(request_payload=request_payload)
        logging.debug(f"Accont ftm balance for {address} is {response}")
        return response

    async def get_ftm_balance_for_multiple_addresses(self, addresses: List[str]):
        logging.info(f"try to get ftm balances for {addresses}")
        addresses = ",".join(addresses)
        request_payload: GetFtmBalanceAddressInterface = {
            "module": "account",
            "action": "balancemulti",
            "address": addresses,
        }
        response = await self.send_request(request_payload=request_payload)
        return response

    async def get_erc_20_token_account_balance_by_contract_address(
        self, address: str, contract_address: str
    ) -> Dict:
        """
        https://api.ftmscan.com/api
        ?module=account
        &action=tokenbalance
        &contractaddress=8394545019028224261891720
        &address=0x5a411f084faa3259924a4764ff9b090c5780a159
        &tag=latest
        &apikey=YourApiKeyToken
        """

        logging.info(f"try to get ftm balance for {address}")
        request_payload = {
            "module": "account",
            "action": "tokenbalance",
            "contractaddress": contract_address,
            "address": address,
        }
        response = await self.send_request(request_payload=request_payload)
        logging.debug(f"Accont ftm balance for {address} is {response}")
        return response
