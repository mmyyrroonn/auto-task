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
from logger import logger
import pyperclip
import random
import pyautogui  #<== need this to click on extension
import time
from basic_operator import (
click, fetch_value,
fetch_content,input_content,
clear_windows_and_resize,switch_to_metamask,
check_element_content,input_password_and_unlock,
metamask_click, switch_to_network, switch_to_page)
from tasks.simple_tasks import follow_user

def bitcraft_register(driver, user, option):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://hub.bitcraftonline.com/ref/4QNXY2TA")
    handle = user['twitter'].split("----")[0].rstrip()
    email = user['discord'].split("：")[1].rstrip().split("---")[0].rstrip()
    logger.info("email is {}, handle is {} for {}".format(email, handle, user["acc_id"]))
    time.sleep(5)
    input_content(driver, "/html/body/div[1]/div/div/div/div/form/input[5]", email)
    time.sleep(1)
    click(driver, "/html/body/div[1]/div/div/div/div/form/button")
    time.sleep(5)
    driver.get("https://outlook.live.com/mail/0/junkemail")
    switch_to_page(driver, "https://hub.bitcraftonline.com/onboarding/steps")
    input_content(driver, "/html/body/div[1]/div/div/div/div/form/input[6]", handle)
    click(driver, "/html/body/div[1]/div/div/div/div/form/button")
    click(driver, "/html/body/div[1]/div/div/div/div/form/div[1]/div[1]/input")
    click(driver, "/html/body/div[1]/div/div/div/div/form/div[1]/div[2]/input")
    click(driver, "/html/body/div[1]/div/div/div/div/form/div[1]/div[3]/input")
    click(driver, "/html/body/div[1]/div/div/div/div/form/div[2]/button")
    result = check_element_content(driver, "/html/body/div[1]/div[2]/aside/div[1]/div", "Alpha Hub", 20)
    logger.info("bitcraft register is {}".format(result))
    return result

def alchemy_register(driver, user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://auth.alchemy.com/signup")
    handle = user['twitter'].split("----")[0].rstrip()
    email = user['discord'].split("：")[1].rstrip().split("---")[0].rstrip()
    logger.info("email is {}, handle is {} for {}".format(email, handle, user["acc_id"]))
    time.sleep(5)
    input_content(driver, "/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div/div[2]/form/label[1]/input", handle)
    input_content(driver, "/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div/div[2]/form/label[2]/input", handle)
    input_content(driver, "/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div/div[2]/form/label[3]/input", email)
    input_content(driver, "/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div/div[2]/form/label[4]/input", password)
    click(driver, "/html/body/div[1]/div/div/div/div/form/button")
    time.sleep(5)
    driver.get("https://outlook.live.com/mail/0/junkemail")
    switch_to_page(driver, "https://hub.bitcraftonline.com/onboarding/steps")
    input_content(driver, "/html/body/div[1]/div/div/div/div/form/input[6]", handle)
    click(driver, "/html/body/div[1]/div/div/div/div/form/button")
    click(driver, "/html/body/div[1]/div/div/div/div/form/div[1]/div[1]/input")
    click(driver, "/html/body/div[1]/div/div/div/div/form/div[1]/div[2]/input")
    click(driver, "/html/body/div[1]/div/div/div/div/form/div[1]/div[3]/input")
    click(driver, "/html/body/div[1]/div/div/div/div/form/div[2]/button")
    result = check_element_content(driver, "/html/body/div[1]/div[2]/aside/div[1]/div", "Alpha Hub", 20)
    logger.info("bitcraft register is {}".format(result))
    return result

def bitcraft_quests_task(driver, user, option):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    follow_user(driver, "BitCraftOnline")
    time.sleep(2)
    follow_user(driver, "clockwork_labs")
    time.sleep(2)
    driver.get("https://hub.bitcraftonline.com/modules/quests")
    #task1 auth discord
    click(driver, "/html/body/div[1]/div[3]/div/div/div[2]/div/div[1]/a")
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[3]/div[1]/div/div[1]/button")
    switch_to_page(driver, "https://discord.com/oauth2/authorize")
    check_element_content(driver, "/html/body/div[1]/div[3]/div/div/div[2]/div/div[1]/a/a", "Claimable", 120)
    driver.get("https://hub.bitcraftonline.com/modules/quests/43")
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[3]/div[1]/div/button")
    time.sleep(3)
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[2]/a")

    #task2 auth twitter
    click(driver, "/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/a")
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[3]/div[1]/div/div[1]/button")
    switch_to_page(driver, "https://api.twitter.com/oauth/authorize")
    click(driver, "/html/body/div[2]/div/form/fieldset/input[1]")
    check_element_content(driver, "/html/body/div[1]/div[3]/div/div/div[2]/div/div[2]/a/a", "Claimable", 120)
    driver.get("https://hub.bitcraftonline.com/modules/quests/52")
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[3]/div[1]/div/button")
    time.sleep(3)
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[2]/a")

    #task3 follow bit craft online
    click(driver, "/html/body/div[1]/div[3]/div/div/div[2]/div/div[3]/a")
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[3]/div[1]/div/div[2]/div/div/button")
    time.sleep(5)
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[3]/div[1]/div/button")
    time.sleep(3)
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[2]/a")

    #task4 follow bit craft online
    click(driver, "/html/body/div[1]/div[3]/div/div/div[2]/div/div[4]/a")
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[3]/div[1]/div/div[2]/div/div/button")
    time.sleep(5)
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[3]/div[1]/div/button")
    time.sleep(3)
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[2]/a")

    #task5 retweet
    click(driver, "/html/body/div[1]/div[3]/div/div/div[2]/div/div[5]/a")
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[3]/div[1]/div/div[1]/button")
    switch_to_page(driver, "https://twitter.com/BitCraftOnline/status/1765827340100333748")
    driver.get("https://twitter.com/intent/retweet?tweet_id=1765827340100333748")
    click(driver, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span/span")
    time.sleep(5)
    driver.get("https://hub.bitcraftonline.com/modules/quests/55")
    time.sleep(1)
    driver.get("https://hub.bitcraftonline.com/modules/quests/55")
    time.sleep(1)
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[3]/div[1]/div/button")
    time.sleep(3)
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[2]/a")

    #task6 youtube
    click(driver, "/html/body/div[1]/div[3]/div/div/div[2]/div/div[6]/a")
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[3]/div[1]/div/div[1]/button")
    switch_to_page(driver, "https://hub.bitcraftonline.com/modules/quests/70")
    driver.get("https://hub.bitcraftonline.com/modules/quests/70")
    time.sleep(1)
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[3]/div[1]/div/button")
    time.sleep(3)
    click(driver, "/html/body/div[1]/div[3]/div/div/div/div[2]/a")

    driver.get("https://hub.bitcraftonline.com/modules/collection/49")
    click(driver, "/html/body/div[1]/div[3]/div/div/div[2]/button")
    time.sleep(3)
    driver.get("https://hub.bitcraftonline.com/modules/collection/60")
    click(driver, "/html/body/div[1]/div[3]/div/div/div[2]/button")
    time.sleep(3)
    driver.get("https://hub.bitcraftonline.com/modules/collection/61")
    click(driver, "/html/body/div[1]/div[3]/div/div/div[2]/button")
    time.sleep(3)
    result = check_element_content(driver, "/html/body/div[1]/div[2]/aside/div[2]/div/div[2]/div/div/div/div/div[1]", "1350", 10)
    logger.info("bitcraft quest is {} for {}".format(result, user["acc_id"]))
    return True


def claim_nym_token(driver, user, option):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    address = user['dym_address']
    driver.get("https://claim.nim.network/address?q={}".format(address))
    click(driver, "/html/body/dialog[1]/article/footer/form/label/input")
    time.sleep(1)
    click(driver, "/html/body/dialog[1]/article/footer/form/button")
    time.sleep(2)
    driver.get("https://claim.nim.network/address?q={}".format(address))
    result = check_element_content(driver, "/html/body/main/form/article/h2", "Your claim is being processed", 20)
    logger.info("claim nym is {} for {}".format(result, user["acc_id"]))
    return result

def humanity_register(driver, user, option):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://cfh.xyz/?ref_id=YBFQZ7JDV")
    handle = user['twitter'].split("----")[0].rstrip()
    email = user['discord'].split("：")[1].rstrip().split("---")[0].rstrip()
    logger.info("email is {}, handle is {} for {}".format(email, handle, user["acc_id"]))
    time.sleep(15)
    click(driver, "/html/body/div[1]/section/div/div[2]/div/div[2]/div[2]")
    input_content(driver, "/html/body/div[1]/section/div/div[24]/div[1]/div/div[2]/div/div[1]/div/input", email)
    input_content(driver, "/html/body/div[1]/section/div/div[24]/div[1]/div/div[2]/div/div[2]/div/input", handle)
    time.sleep(1)
    click(driver, "/html/body/div[1]/section/div/div[24]/div[1]/div/div[3]/button")
    result = check_element_content(driver, "/html/body/div[1]/section/div/div[24]/div[1]/div/div[1]", "Welcome", 15)
    logger.info("humanity register is {}".format(result))
    return result