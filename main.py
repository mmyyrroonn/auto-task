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
from concurrent.futures import ThreadPoolExecutor
import pyautogui  #<== need this to click on extension
from basic_operator import click,fetch_content,input_content,clear_windows_and_resize
from data_manager import load_users_list
from tasks import (bera_drip, import_discord,
                   import_twitter, follow_users,
                   import_unisat, well3_daily, qna3_daily,
                   daily_bera_galxe_point, well3_daily_mint,
                   nfp_daily_check)

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
            print("Already started and skip it")
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
        print("Close it")

    def connect(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", self.selemium)
        service = ChromeService(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        return self.driver
    
class Executor:
    def __init__(self) -> None:
        self.users_list = load_users_list()
        pass

    def run_once(self, task_func, user, *args, **kwargs):
        chrome = AdsPowerChromeDriver(user['user_id'])
        try:
            chrome.start()
            print(chrome.selemium)
            print(chrome.driver_path)
            driver = chrome.connect()
            time.sleep(1)
            clear_windows_and_resize(driver)
            time.sleep(0.5)
            task_func(driver, user, *args, **kwargs)
            time.sleep(2)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            chrome.close()

    def sequence_run_tasks(self, task_func, start_user_index=0, *args, **kwargs):
        users = self.users_list[start_user_index:]
        for user in users:
            self.run_once(task_func, user, *args, **kwargs)

    def batch_run_tasks(self, task_func, start_user_index=0, max_count = 5, *args, **kwargs):
        users = self.users_list[start_user_index:]
        pool = ThreadPoolExecutor(max_workers=max_count)

        # 提交任务到线程池
        futures = []
        count = 0
        for user in users:
            future = pool.submit(self.run_once, task_func, user, *args, **kwargs)
            time.sleep(2)
            futures.append(future)
            count += 1
            if(count == max_count):
                for future in futures:
                    future.result()
                count = 0
                futures = []

        for future in futures:
            future.result()

        # 关闭线程池
        pool.shutdown()

def sequence_follow_twitter():
    users_list = load_users_list()
    user_ids = [user['twitter'].split("----")[0] for user in users_list]
    users = users_list[4:]
    for user in users:
        print(user)
        chrome = AdsPowerChromeDriver(user['user_id']) #, "127.0.0.1:5259", "C:\\Users\\myron\\AppData\\Roaming\\adspower_global\\cwd_global\\chrome_119\\chromedriver.exe")
        chrome.start()
        print(chrome.selemium)
        print(chrome.driver_path)
        driver = chrome.connect()
        time.sleep(1)
        clear_windows_and_resize(driver)
        time.sleep(0.5)
        # Randomly selecting 20 unique user_ids (or fewer if there aren't enough)
        following = random.sample(user_ids, min(len(user_ids), 20))
        follow_users(driver, user, following)
        chrome.close()


executor = Executor()
executor.batch_run_tasks(daily_bera_galxe_point, 0, 5, password)
executor.batch_run_tasks(well3_daily_mint, 0, 2, password)
executor.batch_run_tasks(bera_drip)
executor.batch_run_tasks(qna3_daily, 0, 5, password)
executor.batch_run_tasks(nfp_daily_check, 0, 3, password)
executor.batch_run_tasks(well3_daily)