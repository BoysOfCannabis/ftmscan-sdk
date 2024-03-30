import asyncio

from module.account import Account


async def main():
    account = Account(API_KEY="NPXXZH1CHCB1E8UR41EVYSRMGYUT5VSTI6")

    balance = await account.get_ftm_balance_for_single_address(
        address="0x9B2Bb6290fb910a960Ec344cDf2ae60ba89647f6"
    )
    print("FTM Balance:", balance)


asyncio.run(main())
