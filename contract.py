import asyncio
import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import questionary
from loguru import logger
from questionary import Choice

from settings import (
    RANDOM_WALLET,
    SLEEP_TO,
    SLEEP_FROM,
    QUANTITY_THREADS,
    THREAD_SLEEP_FROM,
    THREAD_SLEEP_TO,
    SAVE_LOGS,
    CHECK_QUESTS_PROGRESS
)
from modules_settings import *
from utils.sleeping import sleep
from utils.logs_handler import filter_out_utils
from utils.password_handler import get_wallet_data
from utils.progress_checker import LineaScan
from itertools import count
import threading
from config import HEADER

def get_module():
    counter = count(1)
    result = questionary.select(
        "Select a method to get started",
        choices=[
            Choice(f"{next(counter)}) Encrypt private keys", encrypt_privates),

            Choice(f"Exit", "exit"),
        ],
        qmark="⚙️ ",
        pointer="✅ "
    ).ask()
    if result == "exit":
        print("❤️ Author – https://t.me/block_nine\n")
        sys.exit()
    return result


def get_wallets():
    wallets_data = get_wallet_data()
    return list(wallets_data.values())


async def run_module(module, wallet_data):
    try:
        await module(wallet_data)
    except Exception as e:
        logger.error(e)
        import traceback

        traceback.print_exc()

    await sleep(SLEEP_FROM, SLEEP_TO)


def _async_run_module(module, wallet_data):
    asyncio.run(run_module(module, wallet_data))


def main(module):
    wallets_data = get_wallets()


    if RANDOM_WALLET:
        random.shuffle(wallets_data)

    with ThreadPoolExecutor(max_workers=QUANTITY_THREADS) as executor:
        for _, wallet_data in enumerate(wallets_data, start=1):
            executor.submit(
                _async_run_module,
                module,
                wallet_data
            )
            time.sleep(random.randint(THREAD_SLEEP_FROM, THREAD_SLEEP_TO))


if __name__ == '__main__':
    print(HEADER)
    if SAVE_LOGS:
        logger.add('logs.txt', filter=filter_out_utils)

    module = get_module()
    main(module)

    print("ALL DONE")