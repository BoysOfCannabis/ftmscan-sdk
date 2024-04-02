from typing import List

from client import FTMExplorerClient
from utils.custom_logger import logger as logging

from .account_typing import GetFtmBalanceForSingleAddressInterface


class Account(FTMExplorerClient):

    async def get_ftm_balance_for_single_address(self, address: str):

        logging.info(f"try to get ftm balance for {address}")
        request_payload: GetFtmBalanceForSingleAddressInterface = {
            "module": "account",
            "action": "balance",
            "address": address,
        }
        response = await self.send_request(request_payload=request_payload)
        logging.debug(f"Accont ftm balance for {address} is {response}")
        return response

    async def get_ftm_balance_for_multiple_addresses(self, addresses: List[str]):
        logging.info(f"try to get ftm balances for {addresses}")

    def get_token_balance(self, token_contract: str, address: str):
        """
        token_contract example: "0xDE1E704dae0B4051e80DAbB26ab6ad6c12262DA0"
        """
