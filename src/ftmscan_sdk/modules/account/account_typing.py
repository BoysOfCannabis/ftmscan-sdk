from typing import List, Literal, TypedDict

ModuleType = Literal["account", "transaction", "contract"]
ActionType = Literal["balance", "balancemulti"]


class BaseFtmPayloadInterface(TypedDict):
    module: ModuleType
    action: ActionType


class GetFtmBalanceAddressInterface(BaseFtmPayloadInterface):
    address: str
