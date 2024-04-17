# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import requests
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import pyautogui  #<== need this to click on extension
from basic_operator import click,fetch_content,input_content,clear_windows_and_resize
from data_manager import load_users_list
from tasks.simple_tasks import (bera_drip, import_discord,
                   import_twitter, follow_users,
                   import_unisat, well3_daily, qna3_daily,
                   daily_bera_galxe_point, well3_daily_mint,
                   nfp_daily_check, test_daily, keplr_import,
                   okx_wallet_import, well3_daily_ai_mint,
                   ultiverse_daily_explore, google_login,
                   transfer_eth_to_ok_coin, palio_daily, sub_wallet_import)
from tasks.onetime_tasks import (bitcraft_register, bitcraft_quests_task, sell_pink, bridge_usdc_to_arb)
from tasks.zksync import (era_land_eth, okx_wallet_exchange, mav_exchange, tevaera_nft_mint,
                          dmail_send_message, odos_exchange, izumi_swap, zero_land_lending)
from tasks.secwarex import (init_connect_and_scan)
from tasks.zeta_tasks import (zetahub_register)
import random
from task_manager import (DailyTaskManager, OnceTaskManager)
from logger import logger

# 加载 .env 文件
load_dotenv()

# 使用环境变量
import os
import time
import random

adspower_address = "http://local.adspower.net:50325"
password = os.environ["password"]

class AdsPowerChromeDriver:
    def __init__(self, user_id, selemium = None, driver_path = None) -> None:
        self.user_id = user_id
        self.selemium = selemium
        self.driver_path = driver_path
        self.driver = None

    def start(self):
        if(self.selemium != None and self.driver_path != None):
            logger.debug("Already started and skip it")
        url = adspower_address + "/api/v1/browser/start"
        params = {
            "user_id": self.user_id
        }
        response = requests.get(url, params=params)

        self.selemium = response.json()['data']['ws']['selenium']
        self.driver_path = response.json()['data']['webdriver']
        time.sleep(5)

    def close(self):
        url = adspower_address + "/api/v1/browser/stop"
        params = {
            "user_id": self.user_id
        }
        _response = requests.get(url, params=params)
        self.selemium = None
        self.driver_path = None
        logger.debug("Close it")

    def get_status(self):
        url = adspower_address + "/api/v1/browser/active"
        params = {
            "user_id": self.user_id
        }
        response = requests.get(url, params=params).json()
        isSuccess = response['code'] == 0
        isActive = isSuccess and response['data']['status'] == "Active"
        return isSuccess, isActive

    def connect(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", self.selemium)
        service = ChromeService(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        return self.driver
    
class Executor:
    def __init__(self, task_manager) -> None:
        self.users_list = load_users_list()
        self.task_manager = task_manager
        pass

    def run_once(self, task_func, user, option, *args, **kwargs):
        chrome = AdsPowerChromeDriver(user['user_id'])
        result = False
        try:
            chrome.start()
            logger.debug(chrome.selemium)
            logger.debug(chrome.driver_path)
            driver = chrome.connect()
            time.sleep(1)
            clear_windows_and_resize(driver)
            time.sleep(0.5)
            result = task_func(driver, user, option)
            time.sleep(2)
        except Exception as e:
            logger.error("An error occurred for {} in task {}".format(user['acc_id'], task_func))
            logger.debug(e)
        finally:
            isManula = kwargs.get('human', False)
            if not result and isManula:
                logger.info("wait operations for {} in task {}".format(user['acc_id'], task_func))
                result = self.wait_for_manually_close(chrome)
                logger.info("finish operations for {} in task {}".format(user['acc_id'], task_func))
            else:
                chrome.close()
        return result
    
    def wait_for_manually_close(self, chrome):
        count = 0
        time.sleep(random.choice([1,2,3,4,5]))
        while True:
            isSuccess, isActive = chrome.get_status()
            if not isSuccess:
                return False
            if not isActive:
                return True
            time.sleep(5)
            count+=1
            if count > 100: # timeout, force quit without success
                return False

    def sequence_run_tasks(self, task_func, option=None, start_user_index=0, *args, **kwargs):
        users = self.users_list[start_user_index:]
        for user in users:
            self.run_once(task_func, user, option, *args, **kwargs)
    
    def sequence_run_tasks_without_driver(self, task_func, option=None, start_user_index=0, *args, **kwargs):
        users = self.users_list[start_user_index:]
        for user in users:
            self.run_once_without_driver(task_func, user, option, *args, **kwargs)

    def run_once_without_driver(self, task_func, user, option, *args, **kwargs):
        result = False
        try:
            result = task_func(None, user, option)
            time.sleep(2)
        except Exception as e:
            logger.error("An error occurred for {} in task {}".format(user['acc_id'], task_func))
            print(e)
        finally:
            logger.info("Wait for a while")
            time.sleep(180)
        return result

    def batch_run_tasks(self, task_func, option=None, start_user_index=0, max_count=5, *args, **kwargs):
        users = self.users_list[start_user_index:]
        with ThreadPoolExecutor(max_workers=max_count) as pool:
            # Dictionary to keep track of which user each future is processing
            future_to_user = {}

            # Submit initial batch of tasks
            for user in users[:max_count]:
                future = pool.submit(self.run_once, task_func, user, option, *args, **kwargs)
                time.sleep(1)
                future_to_user[future] = user

            # Process remaining users
            for user in users[max_count:]:
                # Wait for the next future to complete before submitting a new one
                done_future = next(as_completed(future_to_user))
                done_future.result()  # You may handle results or exceptions here

                time.sleep(1)
                # Submit a new task to the pool
                future = pool.submit(self.run_once, task_func, user, option, *args, **kwargs)
                future_to_user[future] = user

                # Remove the completed future from the dictionary
                del future_to_user[done_future]

            # Wait for the remaining futures to complete
            for future in as_completed(future_to_user):
                future.result()  # Again, handle results or exceptions if necessary

    def random_run_all_tasks(self, task_func_with_option_list, max_count=5, retry=3, *args, **kwargs):
        for i in range(retry): # to deal with failure
            tasks = self.task_manager.build_task_list(self.users_list, task_func_with_option_list)
            with ThreadPoolExecutor(max_workers=max_count) as pool:
                # Dictionary to keep track of which user each future is processing
                future_to_task = {}

                # Submit initial batch of tasks
                for task in tasks[:max_count]:
                    future = pool.submit(self.run_once, task["func"], task["user"], task["option"], *args, **kwargs)
                    time.sleep(1)
                    future_to_task[future] = task

                # Process remaining users
                for task in tasks[max_count:]:
                    # Wait for the next future to complete before submitting a new one
                    done_future = next(as_completed(future_to_task))
                    self.task_manager.handle_result(done_future.result(), future_to_task[done_future])
                    time.sleep(1)
                    # Submit a new task to the pool
                    future = pool.submit(self.run_once, task["func"], task["user"], task["option"], *args, **kwargs)
                    future_to_task[future] = task

                    # Remove the completed future from the dictionary
                    del future_to_task[done_future]

                # Wait for the remaining futures to complete
                for future in as_completed(future_to_task):
                    self.task_manager.handle_result(future.result(), future_to_task[future])
        tasks = self.task_manager.build_task_list(self.users_list, task_func_with_option_list)
        logger.info("Remaining tasks is {}".format(len(tasks)))

executor = Executor(DailyTaskManager())
executor.sequence_run_tasks(zero_land_lending, {"password": password}, 15)
# # executor.batch_run_tasks(well3_daily_ai_mint, {"password": password}, 10, 5)

# task_func_with_option_list = [(well3_daily_mint, {"password": password}, [x for x in range(1, 51)]),
#                               (nfp_daily_check, {"password": password}, [x for x in range(1, 51)]),
#                               (well3_daily_ai_mint, {"password": password}, [x for x in range(1, 51)]),
#                               (ultiverse_daily_explore, {"password": password}, [x for x in range(1, 51)]),
#                               (well3_daily, None, [x for x in range(1, 51)]),
#                               (palio_daily, {"password": password}, [x for x in range(1, 9)])]
# executor.random_run_all_tasks(task_func_with_option_list, human=True)


# once_executor = Executor(OnceTaskManager())
# zksync_task_function_list = [(era_land_eth, {"password": password}, [x for x in range(1, 51)]),
#                               (okx_wallet_exchange, {"password": password}, [x for x in range(1, 51)]),
#                               (mav_exchange, {"password": password}, [x for x in range(1, 51)]),
#                               (tevaera_nft_mint, {"password": password}, [x for x in range(1, 51)]),
#                               (dmail_send_message, {"password": password}, [x for x in range(1, 51)]),
#                               (odos_exchange, {"password": password}, [x for x in range(1, 51)]),
#                               (izumi_swap, {"password": password}, [x for x in range(1, 51)]),
#                               (zero_land_lending, {"password": password}, [x for x in range(1, 51)]),
#                               ]

# once_executor.random_run_all_tasks(zksync_task_function_list, max_count=2, retry=1, human=True)