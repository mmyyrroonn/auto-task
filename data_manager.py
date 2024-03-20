def load_users_list():
    users_list = []
    with open("../user_ids.txt", "r") as file:
        with open("../discord-accounts.txt", "r", encoding='utf-8') as discord:
            with open("../twitter-accounts.txt", "r", encoding='utf-8') as twitter:
                with open("../addresses.txt", "r", encoding='utf-8') as addresses:
                    for index in range(50):
                        acc_id = int(file.readline().split('=')[1].rstrip())
                        user_id = file.readline().split('=')[1].rstrip()
                        name = file.readline().split('=')[1]
                        file.readline()
                        discord_info = discord.readline()
                        twitter_info = twitter.readline()
                        address_info = addresses.readline().rstrip()
                        mnemonic = open("../evm-metamask-seeds-using/{}.json".format(index), "r").readline().split(' ')
                        dym = open("../dym/{}.json".format(index+1), "r").readline().split(' ')
                        users_list.append({"acc_id": acc_id,
                                           "user_id": user_id,
                                           "name": int(name),
                                           "discord": discord_info,
                                           "twitter": twitter_info,
                                           "address": address_info,
                                           "mnemonic": mnemonic,
                                           "dym": dym})
    print("Load user id list")
    print(users_list)
    return users_list