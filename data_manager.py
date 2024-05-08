from utils.general import mnemonic_to_private_key, ETH_DERIVATION_PATH
import binascii

def load_users_list():
    users_list = []
    with open("../user_ids.txt", "r") as file:
        with open("../discord-accounts.txt", "r", encoding='utf-8') as discord:
            with open("../twitter-accounts.txt", "r", encoding='utf-8') as twitter:
                with open("../addresses.txt", "r", encoding='utf-8') as addresses:
                    with open("../dymesion_address.txt", "r", encoding='utf-8') as dym_addresses:
                        with open("../google-accounts.txt", "r", encoding='utf-8') as google_accounts:
                            with open("../ok-mapping.txt", "r", encoding='utf-8') as ok_address:
                                for index in range(50):
                                    acc_id = int(file.readline().split('=')[1].rstrip())
                                    user_id = file.readline().split('=')[1].rstrip()
                                    name = file.readline().split('=')[1]
                                    file.readline()
                                    proxy = file.readline().split('=')[1][:-3]
                                    file.readline()
                                    file.readline()
                                    file.readline()
                                    address_info = addresses.readline().rstrip()
                                    mnemonic = open("../evm-metamask-seeds-using/{}.json".format(index), "r").readline().split(' ')
                                    discord_info = discord.readline()
                                    twitter_info = twitter.readline()
                                    ok_addr = ok_address.readline().rstrip()
                                    dym = open("../dym/{}.json".format(index+1), "r").readline().split(' ')
                                    dym_address_info = dym_addresses.readline().rstrip()
                                    google_account = google_accounts.readline()
                                    users_list.append({"acc_id": acc_id,
                                                    "user_id": user_id,
                                                    "name": int(name),
                                                    "discord": discord_info,
                                                    "twitter": twitter_info,
                                                    "address": address_info,
                                                    "mnemonic": mnemonic,
                                                    "dym": dym,
                                                    "ok_addr": ok_addr,
                                                    "dym_address": dym_address_info,
                                                    "google_account": google_account,
                                                    "proxy": proxy})
                                for index in range(50, 100):
                                    acc_id = int(file.readline().split('=')[1].rstrip())
                                    user_id = file.readline().split('=')[1].rstrip()
                                    name = file.readline().split('=')[1]
                                    file.readline()
                                    proxy = file.readline().split('=')[1][:-3]
                                    file.readline()
                                    file.readline()
                                    file.readline()
                                    address_info = addresses.readline().rstrip()
                                    mnemonic = open("../evm-metamask-seeds-using/{}.json".format(index), "r").readline().split(' ')
                                    # discord_info = discord.readline()
                                    # twitter_info = twitter.readline()
                                    # ok_addr = ok_address.readline().rstrip()
                                    # dym = open("../dym/{}.json".format(index+1), "r").readline().split(' ')
                                    # dym_address_info = dym_addresses.readline().rstrip()
                                    # google_account = google_accounts.readline()
                                    users_list.append({"acc_id": acc_id,
                                                    "user_id": user_id,
                                                    "name": int(name),
                                                    "address": address_info,
                                                    "mnemonic": mnemonic,
                                                    "proxy": proxy})
    add_id(users_list)
    add_okx_address(users_list)
    generate_private_key(users_list)
    print("Load user id list")
    return users_list

def add_id(users_list):
    for user in users_list:
        user["id"] = user["acc_id"]

def add_okx_address(users_list):
    for user in users_list:
        user["okx_address"] = False

def generate_private_key(users_list):
    for user in users_list:
        mnemonic = " ".join(user['mnemonic'])

        # Generate the private key from the seed phrase
        user["private_key"] = mnemonic_to_private_key(mnemonic, str_derivation_path=f'{ETH_DERIVATION_PATH}/0')
        # print(f'privkey: {binascii.hexlify(user["private_key"]).decode("utf-8")}')