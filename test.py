import asyncio

from modules import Account
from utils import logger


async def main():
    account = Account(API_KEY="NPXXZH1CHCB1E8UR41EVYSRMGYUT5VSTI6")

    adresses = [
        "0x9B2Bb6290fb910a960Ec344cDf2ae60ba89647f6",
        "0x9B2Bb6290fb910a960Ec344cDf2ae60ba89647f6",
        "0x9B2Bb6290fb910a960Ec344cDf2ae60ba89647f6",
        "0x9B2Bb6290fb910a960Ec344cDf2ae60ba89647f6",
        "0x9B2Bb6290fb910a960Ec344cDf2ae60ba89647f6",
    ]
    tasks = [
        asyncio.create_task(account.get_ftm_balance_for_single_address(address))
        for address in adresses
    ]
    results = await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
