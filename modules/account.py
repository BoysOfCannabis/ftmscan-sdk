from asyncio import sleep
from typing import Dict, Literal, TypedDict

from modules.client import FTMExplorerClient
from modules.custom_logger import logger as logging

ModuleType = Literal["account", "transaction", "contract"]
ActionType = Literal["balance"]


class RequesePayloadInterface(TypedDict):
    module: ModuleType
    action: ActionType
    address: str


class Account(FTMExplorerClient):

    async def get_ftm_balance_for_single_address(self, address: str):
        logging.info(f"try to get ftm balance for {address}")
        request_payload: RequesePayloadInterface = {
            "module": "account",
            "action": "balance",
            "address": address,
        }
        response = await self.send_request(request_payload=request_payload)
        logging.debug(f"Accont ftm balance for {address} is {response}")
        return response

    def get_token_balance(self, token_contract: str, address: str):
        """
        token_contract example: "0xDE1E704dae0B4051e80DAbB26ab6ad6c12262DA0"
        """
