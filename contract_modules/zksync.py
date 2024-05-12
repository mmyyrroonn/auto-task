import random
from hashlib import sha256

from loguru import logger
from utils.gas_checker import check_gas
from utils.helpers import retry
from .account import Account
from config import TEVAERA_ABI


class Zksync(Account):
    def __init__(self, wallet_info) -> None:
        super().__init__(wallet_info=wallet_info, chain="zksync")

    @retry
    async def tevaera_nft_mint(self):
        logger.info(f"[{self.account_id}][{self.address}] mint tevaera nft")

        contract_address = "0xd29Aa7bdD3cbb32557973daD995A3219D307721f"

        contract_address = self.w3.to_checksum_address(contract_address)
        contract = self.get_contract(contract_address, abi=TEVAERA_ABI)

        balance_wei = await contract.functions.balanceOf(self.address).call()

        if balance_wei > 0:
            logger.info("tevaera_nft_mint is already minted")
            return True

        data = "0xfefe409d"
        amount = self.w3.to_wei(0.0003, "ether")
        tx_data = await self.get_tx_data(value=amount)
        tx_data.update(
            {"data": data, "to": contract_address}
        )

        signed_txn = await self.sign(tx_data)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())

        return True
