import asyncio

from modules import Account
from utils.custom_logger import logger as logging


async def main():
    await get_balance_for_multiple_addresses()


async def get_balance_for_single_address():
    account = Account(API_KEY="NPXXZH1CHCB1E8UR41EVYSRMGYUT5VSTI6")

    address = "0x9B2Bb6290fb910a960Ec344cDf2ae60ba89647f6"
    tasks = asyncio.create_task(account.get_ftm_balance_for_single_address(address))
    results = await asyncio.gather(tasks)


async def get_balance_for_multiple_addresses():
    account = Account(API_KEY="NPXXZH1CHCB1E8UR41EVYSRMGYUT5VSTI6")
    adresses = [
        "0x1B5248B881762576d630246feeA92E5c6FceD2e1",
        "0x48Eb0e2b01c9B35521c6ff877D525D5dcB582671",
    ]
    tasks = asyncio.create_task(
        account.get_ftm_balance_for_multiple_addresses(adresses)
    )

    results = await asyncio.gather(tasks)
    print("results", results)


if __name__ == "__main__":
    asyncio.run(main())
