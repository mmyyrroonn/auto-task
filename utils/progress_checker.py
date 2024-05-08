import random

from loguru import logger

from config import LINEASCAN_URL, LINEA_API_KEYS, PROGRESS_PATH
import requests
from typing import List, Dict
import pandas as pd
from tqdm import tqdm
import time
import os


class LineaScan:
    def __init__(self, wallets_data):
        self.wallets_data = wallets_data

    @staticmethod
    def url_maker(module, action, **kwargs) -> str:

        url = LINEASCAN_URL + f'?module={module}' \
                              f'&action={action}' \
                              f'&apikey={random.choice(LINEA_API_KEYS)}'
        if kwargs:
            for key, value in kwargs.items():
                url += f'&{key}={value}'
        return url

    def get_wallet_transactions(self, address, proxies=None):
        url = self.url_maker('account', 'txlist', address=address)
        if proxies:
            try:
                response = requests.get(url, proxies=proxies, timeout=10)
            except:
                response = requests.get(url)
        else:
            response = requests.get(url)
        res = response.json()
        return res

    @staticmethod
    def parse_transactions(transactions: List[Dict], wallet, df: pd.DataFrame):
        s_universe = 'de240b2a3634fcd72919eb591a7207bddef03cd'
        df.loc[wallet, :] = False
        for tx in transactions:
            if tx['to'] == '0x6cd20be8914a9be48f2a35e56354490b80522856' and tx['methodId'] == '0xb9a2092d':
                df.loc[wallet, 'gamer_boom_proof'] = True
            elif tx['to'] == '0xc0b4ab5cb0fdd6f5dfddb2f7c10c4c6013f97bf2' and tx['methodId'] == '0x1249c58b':
                df.loc[wallet, 'gamer_boom_mint'] = True
            elif tx['to'] == '0x34be5b8c30ee4fde069dc878989686abe9884470' and tx['methodId'] == '0xe139278f':
                df.loc[wallet, 'nidum_mint'] = True
            elif tx['to'] == '0x34be5b8c30ee4fde069dc878989686abe9884470' and tx['methodId'] == '0xf5298aca':
                df.loc[wallet, 'nidum_bonus'] = True
            elif tx['to'] == '0x281a95769916555d1c97036e0331b232b16edabc' and tx['methodId'] == '0xf160619b':
                df.loc[wallet, 'townstory_mint'] = True
            elif tx['to'] == '0xd41ac492fedc671eb965707d1dedad4eb7b6efc5' and tx['methodId'] == '0x48e33382':
                df.loc[wallet, 'travelbag_mint'] = True
            # Week 2
            elif (tx['to'] == '0x66ccc220543b6832f93c2082edd7be19c21df6c0' or
                  tx['to'] == "0x0391c15886b5f74a776b404c82d30eef4be88335") and tx['methodId'] == '0xefef39a1':
                df.loc[wallet, 'abuse_world_mint'] = True
            elif tx['to'] == '0xb18b7847072117ae863f71f9473d555d601eb537' and tx['methodId'] == '0x14f710fe':
                df.loc[wallet, 'pictograph_mint'] = True
            elif tx['to'] == '0xb18b7847072117ae863f71f9473d555d601eb537' and tx['methodId'] == '0xa694fc3a':
                df.loc[wallet, 'pictograph_stake'] = True
            elif tx['to'] == '0xecbee1a087aa83db1fcc6c2c5effc30bcb191589' and s_universe in tx['input']:
                df.loc[wallet, 'satoshi_universe_mint'] = True
            elif tx['to'] == '0x63ce21bd9af8cc603322cb025f26db567de8102b' and tx['methodId'] == '0xfb89f3b1':
                df.loc[wallet, 'yooldo_daily_task'] = True
            # Week 3
            elif tx['to'] == '0xd1a3abf42f9e66be86cfdea8c5c2c74f041c5e14' and (tx['methodId'] == '0x5b7d7482'
                                                                               and tx['timeStamp'] > '1709251200'):
                df.loc[wallet, 'send_mail'] = True
            elif tx['to'] == '0xe5d7c2a44ffddf6b295a15c148167daaaf5cf34f' and tx['methodId'] == '0xd0e30db0':
                df.loc[wallet, 'wrap_eth'] = True
            elif tx['to'] == '0xc043bce9af87004398181a8de46b26e63b29bf99' and (tx['methodId'] == '0xefef39a1'
                                                                               and tx['timeStamp'] > '1709251200'):
                df.loc[wallet, 'asmatch_mint'] = True
            elif tx['to'] == '0x37d4bfc8c583d297a0740d734b271eac9a88ade4' and tx['methodId'] == '0x183ff085':
                df.loc[wallet, 'bitavatar_checkin'] = True
            elif tx['to'] == '0x8286d601a0ed6cf75e067e0614f73a5b9f024151' and tx['methodId'] == '0x7859bb8d':
                df.loc[wallet, 'readon_curate'] = True
            elif tx['to'] == '0x2933749e45796d50eba9a352d29eed6fe58af8bb' and tx['methodId'] == '0xf02bc6d5':
                df.loc[wallet, 'sendingme_send'] = True
            # Week 4
            elif tx['to'] == '0x47874ff0bef601d180a8a653a912ebbe03739a1a' and tx['methodId'] == '0xefef39a1':
                df.loc[wallet, 'sarubol_mint'] = True
            elif tx['to'] == '0x490d76b1e9418a78b5403740bd70dfd4f6007e0f' and tx['methodId'] == '0x36ab86c4':
                df.loc[wallet, 'z2048_start_game'] = True
            elif tx['to'] == '0xc577018b3518cd7763d143d7699b280d6e50fdb6' and tx['methodId'] == '0x70245bdc':
                df.loc[wallet, 'lucky_cat_mint'] = True
            # Week 5
            elif tx['to'] == '0x7136abb0fa3d88e4b4d4ee58fc1dfb8506bb7de7' and tx['methodId'] == '0x1249c58b':
                df.loc[wallet, 'omnizone_mint'] = True
            elif tx['to'] == '0x578705c60609c9f02d8b7c1d83825e2f031e35aa' and tx['methodId'] == '0x6871ee40':
                df.loc[wallet, 'battlemon_mint'] = True
            elif tx['to'] == '0x9df3c2c75a92069b99c73bd386961631f143727c' and tx['methodId'] == '0x57bc3d78':
                df.loc[wallet, 'play_nouns'] = True
            # Week 6
            elif tx['to'] == '0x971a871fd8811abbb1f5e3fb1d84a873d381cee4' and tx['methodId'] == '0xbaeb0718':
                df.loc[wallet, 'zace_check_in'] = True
            elif tx['to'] == '0x915d2358192f5429fa6ee6a6e5d1b37026d580ba' and tx['methodId'] == '0xefef39a1':
                df.loc[wallet, 'micro3_mint'] = True
            elif tx['to'] == '0x5ecde77c11e52872adeb3ef3565ffa0b2bcc1c68' and tx['methodId'] == '0xefef39a1':
                df.loc[wallet, 'alienswap_mint'] = True
            elif tx['to'] == '0xea81a18fb97401a9f4b79963090c65a3a30ecdce' and tx['methodId'] == '0x57bc3d78':
                df.loc[wallet, 'frog_war_mint'] = True
            elif tx['to'] == '0x184e5677890c5add563de785ff371f6c188d3db6' and tx['methodId'] == '0x57bc3d78':
                df.loc[wallet, 'frog_war_bonus'] = True
            elif tx['to'] == '0xcd1ea9e70d0260c0f47d217ed6d5be9cd4ed34fb' and tx['methodId'] == '0x1249c58b':
                df.loc[wallet, 'acg_worlds_mint'] = True
            elif tx['to'] == '0xa091303966ef5f94cf68f85d892c729fd6c3f30b' and tx['methodId'] == '0x738a9fa1':
                df.loc[wallet, 'bilinear_mint'] = True
            elif tx['to'] == '0xb99e5534d42500eb1d5820fba3bb8416ccb76396' and tx['methodId'] == '0xd85d3d27':
                df.loc[wallet, 'imagineairynfts_mint'] = True
            elif tx['to'] == '0xbd0ef89f141680b9b2417e4384fdf73cfc696f9f' and tx['methodId'] == '0x40d097c3':
                df.loc[wallet, 'arenagames_mint'] = True

    def wait_transactions(self, address, all_proxies):
        n_attemps = 10
        while n_attemps:
            proxy = random.choice(all_proxies)
            proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
            transactions = self.get_wallet_transactions(address.lower(), proxies)
            if transactions['status'] == 1:
                return transactions
            n_attemps -= 1
            time.sleep(5)

    def get_wallet_progress(self, replace=False):
        if os.path.exists(PROGRESS_PATH) and not replace:
            logger.info(f'Load progress from {PROGRESS_PATH}')
            return
        logger.info('Check quests progress from blockchain data')

        cols = ['gamer_boom_proof', 'gamer_boom_mint', 'nidum_mint', 'nidum_bonus', 'townstory_mint', 'travelbag_mint',
                'abuse_world_mint', 'pictograph_mint', 'pictograph_stake', 'satoshi_universe_mint', 'yooldo_daily_task',
                'send_mail', 'wrap_eth', 'asmatch_mint', 'bitavatar_checkin', 'readon_curate', 'sendingme_send',
                'sarubol_mint', 'z2048_start_game', 'lucky_cat_mint', 'omnizone_mint', 'battlemon_mint', 'play_nouns',
                'zace_check_in', 'micro3_mint', 'alienswap_mint', 'frog_war_mint', 'frog_war_bonus',
                'acg_worlds_mint', 'bilinear_mint', 'imagineairynfts_mint', 'arenagames_mint']

        df = pd.DataFrame(columns=cols)
        all_proxies = [wallet_info['proxy'] for wallet_info in self.wallets_data]
        for wallet_info in tqdm(self.wallets_data):
            address = wallet_info['address'].lower()
            proxies = {'http': f'http://{wallet_info["proxy"]}', 'https': f'http://{wallet_info["proxy"]}'}
            try:
                transactions = self.get_wallet_transactions(address, proxies)
                if transactions['status'] != '1':
                    transactions = self.wait_transactions(address, all_proxies)
            except:
                transactions = self.wait_transactions(address, all_proxies)
            try:
                if transactions['status'] == '1':
                    self.parse_transactions(transactions['result'][:100], wallet_info['address'], df)
                else:
                    print(transactions)
            except Exception as e:
                logger.warning(f'Can not parse {address} wallet. Error: {e}')
        df.fillna(False).to_excel('progress.xlsx')
