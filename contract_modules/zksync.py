import random
from hashlib import sha256

from loguru import logger
from utils.gas_checker import check_gas
from utils.helpers import retry
from .account import Account


class Zksync(Account):
    def __init__(self, wallet_info) -> None:
        super().__init__(wallet_info=wallet_info, chain="zksync")

    @retry
    async def tevaera_nft_mint(self):
        logger.info(f"[{self.account_id}][{self.address}] mint tevaera nft")

        contract = "0xd29Aa7bdD3cbb32557973daD995A3219D307721f"

        data = "0xfefe409d"
        amount = self.w3.to_wei(0.0003, "ether")
        tx_data = await self.get_tx_data(value=amount)
        tx_data.update(
            {"data": data, "to": self.w3.to_checksum_address(contract)}
        )

        signed_txn = await self.sign(tx_data)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())

        return True
    
async def tevaera_nft_mint(wallet_info):
    """
    Task 3
    """

    zksync_inst = Zksync(wallet_info)
    return await zksync_inst.tevaera_nft_mint()
