import asyncio
from utils.progress_checker import LineaScan
from contract_modules import *


########################################################################
#                          Setup Modules                               #
########################################################################

async def withdraw_okx(wallet_info):
    """
    Withdraw ETH from OKX

    WARNING! OKX DOES NOT SUPPORT SCROLL CHAIN
    ______________________________________________________
    min_amount - min amount (ETH)
    max_amount - max_amount (ETH)
    chains - ['zksync', 'arbitrum', 'linea', 'base', 'optimism']
    terminate - if True - terminate program if money is not withdrawn
    skip_enabled - If True, the skip_threshold check will be applied; otherwise, it will be ignored
    skip_threshold - If skip_enabled is True and the wallet balance is greater than or equal to this threshold,
                     skip the withdrawal
    """
    token = 'ETH'
    chains = ['linea']

    min_amount = 0.0023
    max_amount = 0.003

    terminate = False

    skip_enabled = False
    skip_threshold = 0.005

    wait_unlimited_time = False
    sleep_between_attempts = [10, 20]  # min, max

    okx_exchange = Okx(wallet_info, chains)
    return await okx_exchange.okx_withdraw(
        min_amount, max_amount, token, terminate, skip_enabled, skip_threshold,
        wait_unlimited_time, sleep_between_attempts
    )


async def transfer_to_okx(wallet_info):
    from_chains = ["optimism", "arbitrum"]

    min_amount = 0.0012
    max_amount = 0.0012
    decimal = 4

    all_amount = True

    min_percent = 100
    max_percent = 100

    save_funds = [0.0001, 0.00012]
    min_required_amount = 0.002

    bridge_from_all_chains = True
    sleep_between_transfers = [120, 350]

    transfer_inst = Transfer(wallet_info)
    return await transfer_inst.transfer_eth(
        from_chains, min_amount, max_amount, decimal, all_amount, min_percent,
        max_percent, save_funds, False, 0, min_required_amount,
        bridge_from_all_chains=bridge_from_all_chains,
        sleep_between_transfers=sleep_between_transfers
    )


async def bridge_orbiter(wallet_info):
    """
    Bridge from orbiter
    ______________________________________________________
    from_chains – source chain - ethereum, polygon_zkevm, arbitrum, optimism, zksync | Select one or more
                  If more than one chain is specified, the software will check the balance in each network and
                  select the chain with the highest balance.
    to_chain – destination chain - ethereum, polygon_zkevm, arbitrum, optimism, zksync | Select one

    min_amount - the minimum possible amount for sending
    max_amount - maximum possible amount to send
    decimal - to which digit to round the amount to be sent

    all_amount - if True, percentage values will be used for sending (min_percent, max_percent
                 instead of min_amount, max_amount).

    min_percent - the minimum possible percentage of the balance to be sent
    max_percent - the maximum possible percentage of the balance to send

    check_balance_on_dest - if True, it will check the balance in the destination network.
    check_amount - amount to check the balance in the destination network. if the balance is greater than this amount,
                   the bridge will not be executed.
    save_funds - what amount to leave in the outgoing network [min, max], chosen randomly from the range
    min_required_amount - the minimum required balance in the network to make the bridge.
                          if there is no network with the required balance, the bridge will not be made
    bridge_from_all_chains - if True, will be produced from all chains specified in the parameter from_chains
    sleep_between_transfers - only if bridge_from_all_chains=True. sleep between few transfers
    """

    from_chains = ["arbitrum", "optimism", "base"]
    to_chain = "linea"

    min_amount = 0.005
    max_amount = 0.0051
    decimal = 6

    all_amount = True

    min_percent = 98
    max_percent = 100

    check_balance_on_dest = True
    check_amount = 0.005
    save_funds = [0.0011, 0.0013]
    min_required_amount = 0.005

    bridge_from_all_chains = False
    sleep_between_transfers = [120, 300]

    orbiter_inst = Orbiter(wallet_info)
    return await orbiter_inst.transfer_eth(
        from_chains, min_amount, max_amount, decimal, all_amount, min_percent, max_percent, save_funds,
        check_balance_on_dest, check_amount, min_required_amount, to_chain, bridge_from_all_chains,
        sleep_between_transfers=sleep_between_transfers
    )


async def deposit_layerbank(wallet_info):
    """
    Make deposit on LayerBank
    ______________________________________________________
    min_amount - the minimum possible amount for deposit
    max_amount - maximum possible amount for deposit
    decimal - to which digit to round the amount to be deposited

    make_withdraw - True, if need withdraw after deposit
    required_amount_for_withdraw - if less than parameter - skip withdrawal
    sleep_from, sleep_to - minimum/maximum delay before withdrawal (if make_withdraw = True)

    all_amount - if True, percentage values will be used for deposit (min_percent, max_percent
                 instead of min_amount, max_amount).

    min_percent - the minimum possible percentage of the balance for deposit
    max_percent - the maximum possible percentage of the balance for deposit


    all_amount - deposit from min_percent to max_percent
    """
    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    make_withdraw = True
    required_amount_for_withdraw = 0.001

    sleep_from = 30
    sleep_to = 60

    all_amount = False

    min_percent = 5
    max_percent = 35

    layerbank_inst = LayerBank(wallet_info)
    await layerbank_inst.router(
        min_amount, max_amount, decimal, sleep_from, sleep_to, make_withdraw, all_amount, min_percent, max_percent,
        required_amount_for_withdraw=required_amount_for_withdraw
    )


async def withdraw_layerbank(wallet_info):
    required_amount_for_withdraw = 0.001

    layerbank_inst = LayerBank(wallet_info)
    await layerbank_inst.withdraw(required_amount_for_withdraw)

async def tevaera_nft_mint(wallet_info, _option):

    zksync_inst = Zksync(wallet_info)
    return await zksync_inst.tevaera_nft_mint()
########################################################################
#                             Checker                                  #
########################################################################
def progress_check(wallets_data):

    replace = True

    LineaScan(wallets_data).get_wallet_progress(replace)
