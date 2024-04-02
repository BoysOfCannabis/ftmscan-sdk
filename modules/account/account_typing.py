from typing import Literal, TypedDict

ModuleType = Literal["account", "transaction", "contract"]
ActionType = Literal["balance"]


class BaseFtmPayloadInterface(TypedDict):
    module: ModuleType
    action: ActionType


class GetFtmBalanceForSingleAddressInterface(BaseFtmPayloadInterface):
    address: str
