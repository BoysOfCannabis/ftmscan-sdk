from typing import Literal

from main import FTMExplorerClient

ModuleType = Literal["account", "transaction", "contract"]
ActionType = Literal["balance"]


class RequesePayloadInterface:
    module: ModuleType
    action: ActionType
    address: str


class Account(FTMExplorerClient):

    def get_ftm_balance_for_single_address(self, address: str):
        request_payload: RequesePayloadInterface = {
            "module": "account",
            "action": "balance",
            "address": address,
        }
        response = self.send_request(request_payload=request_payload)
        return response
