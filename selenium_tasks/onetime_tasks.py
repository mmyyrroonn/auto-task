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
from loguru import logger
import pyperclip
import random
import pyautogui  #<== need this to click on extension
import time
from basic_operator import (
click, fetch_attribute,
fetch_content,input_content,
clear_windows_and_resize,
check_element_content,input_password_and_unlock,
metamask_click, switch_to_network, switch_to_page,
switch_to_okwallet, input_password_and_unlock_okxwallet, okxwallet_click)
from selenium_tasks.simple_tasks import follow_user

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

def sell_pink(driver, user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://app.stellaswap.com/zh-CN/exchange/swap")
    click(driver, "/html/body/div/div/header/nav/div/div/div[2]/div/div[3]/button")
    click(driver, "/html/body/reach-portal/div[3]/div/div/div/div/div/div/div[3]/div[1]/div[1]")
    switch_to_okwallet(driver)
    input_password_and_unlock_okxwallet(driver, password)
    okxwallet_click(driver,
                    ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                             ],
                    30)
    driver.switch_to.window(driver.window_handles[0])
    click(driver, "/html/body/div/div/main/section/div[2]/div/div[2]/div[1]/div/div[1]/button/div/div[2]/div[2]/div")
    input_content(driver, "/html/body/reach-portal/div[3]/div/div/div/div/div/div/div[2]/input", "pink")
    time.sleep(1)
    click(driver, "/html/body/reach-portal/div[3]/div/div/div/div/div/div/div[4]/div[1]/div/div/div")
    time.sleep(1)
    click(driver, "/html/body/div/div/main/section/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/span[2]")
    time.sleep(5)
    click(driver, "/html/body/div/div/main/section/div[2]/div/div[3]/div/button")
    switch_to_okwallet(driver)
    click(driver, "/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/div[1]/div/div[3]")
    click(driver, "/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]")
    input_content(driver, "/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/input[2]", "40000")
    click(driver, "/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/button")
    okxwallet_click(driver,
                    ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                     "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                             ],
                    30)
    driver.switch_to.window(driver.window_handles[0])
    _ = check_element_content(driver, "/html/body/div/div/main/section/div[2]/div/div[3]/button", "Swap", 30)
    click(driver, "/html/body/div/div/main/section/div[2]/div/div[3]/button")
    click(driver, "/html/body/reach-portal[2]/div[3]/div/div/div/div/div/div/div[3]/button")
    okxwallet_click(driver,
                    ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                     "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                             ],
                    30)
    result = check_element_content(driver, "/html/body/div/div/main/section/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/span[2]", "0.00", 60)
    logger.info("sell pink is {} for {}".format(result, user['acc_id']))
    return result


def bridge_usdc_to_arb(driver, user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://app.stellaswap.com/zh-CN/exchange/cross-chain-swap")
    # click(driver, "/html/body/div/div/header/nav/div/div/div[2]/div/div[3]/button")
    # click(driver, "/html/body/reach-portal/div[3]/div/div/div/div/div/div/div[3]/div[1]/div[1]")
    switch_to_okwallet(driver)
    input_password_and_unlock_okxwallet(driver, password)
    okxwallet_click(driver,
                    ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                     "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                             ],
                    30)
    driver.switch_to.window(driver.window_handles[0])
    click(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/span[1]/span/span[1]/span[1]/a/button")
    click(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/span[2]/ul/li[2]/button")
    click(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/span[1]/span/span[2]/span/button")
    if not check_element_content(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/span[1]/span/span[1]/span[2]/span[1]/a[1]/span/button/span/span/span", "Moonbeam", 10):
        logger.info("bridge usdc is something wrong for {}".format(user['acc_id']))
        return False

    click(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/span[1]/span/span[3]/span[2]/span[1]/a[1]/span/button")
    click(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/ul/li[3]/button")
    if not check_element_content(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/span[1]/span/span[3]/span[2]/span[1]/a[1]/span/button/span/span/span", "Arbitrum", 10):
        logger.info("bridge usdc is something wrong for {}".format(user['acc_id']))
        return False

    click(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/span[1]/span/span[3]/span[2]/span[1]/a[2]/span/button")
    input_content(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/span/span/input", "USDT")
    click(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/ul/li/button/span[2]/span/span")

    click(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/span[1]/span/span[1]/span[2]/span[3]/span[2]/button")
    _ = check_element_content(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/span[1]/span/span[3]/span[2]/span[2]/span/span/span/span", ".", 30)
    #
    click(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/span[3]/button")
    switch_to_okwallet(driver)
    okxwallet_click(driver,
                    ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                     "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                             ],
                    30)
    driver.switch_to.window(driver.window_handles[0])
    if check_element_content(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/div/span[1]/span/span/span[1]", "Processing", 10):
        result = check_element_content(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/div/span[1]/span/span/span[1]", "Complete", 60)
        logger.info("bridge usdc is {} for {}".format(result, user['acc_id']))
        return result
    _ = check_element_content(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/span[3]/button/span/span/span", "Submit", 60)
    click(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/span[3]/button")
    switch_to_okwallet(driver)
    okxwallet_click(driver,
                    ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                     "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                    ],
                    30)
    driver.switch_to.window(driver.window_handles[0])
    result = check_element_content(driver, "/html/body/div/div/main/section/div[2]/div/div/div[2]/div/span[1]/span/span/span[1]", "Complete", 120)
    logger.info("bridge usdc is {} for {}".format(result, user['acc_id']))
    return result

def well3_nft_open(driver, _user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://well3.com/mission")
    try:
        click(driver, "/html/body/div/button")
    except:
        pass
    click(driver, "/html/body/div/div[1]/header/div/div[1]/a/div/img") # click start
    click(driver, "/html/body/div/div[2]/div/div[2]/div/div/div[1]/div/nav/ol/li[5]/a/span") # click master's wisdom
    click(driver, "/html/body/div/div[1]/main/div/div[2]/div[1]/div[5]/button") # connect wallet
    click(driver, "/html/body/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/button/div/div/div[2]") # click metamask
    switch_to_okwallet(driver)
    input_password_and_unlock_okxwallet(driver, password)
    okxwallet_click(driver,
                    ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                     "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                    ],
                    30)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    if check_element_content(driver, "/html/body/div/div[1]/main/div/div[2]/div[1]/div[5]/button", "Link", 3):
        click(driver, "/html/body/div/div[1]/main/div/div[2]/div[1]/div[5]/button") # Link
        okxwallet_click(driver,
                    ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                     "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                    ],
                    30)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
    if check_element_content(driver, "/html/body/div/div[1]/main/div/div[2]/div[1]/div[5]/button", "Switch", 3):
        click(driver, "/html/body/div/div[1]/main/div/div[2]/div[1]/div[5]/button") # Switch
        okxwallet_click(driver,
                    ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                     "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                    ],
                    30)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
    click(driver, "/html/body/div/div[1]/main/div/div[2]/div[1]/div[5]/div[1]/div[1]") # free
    click(driver, "/html/body/div/div[1]/div[4]/div/div/div/div/div") # mint
    okxwallet_click(driver,
                    ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                     "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                    ],
                    30)
    time.sleep(2)
    logger.info("well3 open mint success")
    return True