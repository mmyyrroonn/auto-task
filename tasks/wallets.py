
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
from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware
from basic_operator import (
click, fetch_attribute,
fetch_content,input_content,
check_element_content,input_password_and_unlock,
metamask_click, switch_to_network, check_content_color,
switch_to_okwallet, input_password_and_unlock_okxwallet, okxwallet_click, okx_wallet_confirm)
#### import metamask
def import_metamask(driver, mnemonic, password):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("chrome-extension://mcgljabdelphdlnplopklpmnjpkhnbho/home.html")
    time.sleep(2)
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/ul/li[1]/div/input').click() # agree to TOS 
    time.sleep(2)
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/ul/li[3]/button').click() # import 
    time.sleep(2)
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div/button[2]').click() # no thanks
    time.sleep(2)
    for i in range(3): driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # locate mnemonic box
    for word in mnemonic:
        driver.switch_to.active_element.send_keys(word) # input each mnemonic to current textbox
        for i in range(2): driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
        # time.sleep(2)
    time.sleep(2)
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button').click() # confirm
    time.sleep(2)
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input').send_keys(password) # enter password
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input').send_keys(password) # enter password twice
    time.sleep(2)
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input').click() # I understand
    driver.find_element('xpath', '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button').click() # import my wallet
    time.sleep(2)
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click() # got it
    time.sleep(2)
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click() # next page
    time.sleep(2)
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click() # done
    time.sleep(2)
    logger.info('import complete')

#### import unisats memo
def import_unisat(driver, user, option):
    password = option["password"]
    mnemonic = user["mnemonic"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("chrome-extension://ppbibelpcjmhbdihakflkdcoccbgbkpo/index.html")
    time.sleep(0.5)
    click(driver, "/html/body/div/div[1]/div/div/div/div[2]/div[3]") # already have
    input_content(driver, "/html/body/div/div[1]/div/div/div/div/div[3]/input", password)
    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
    time.sleep(0.5)
    input_content(driver, "/html/body/div/div[1]/div/div/div/div/div[4]/input", password)
    click(driver, "/html/body/div/div[1]/div/div/div/div/div[5]") # already have
    click(driver, "/html/body/div/div[1]/div/div[2]/div[2]/div[2]") # UniSat Wallet
    for word in mnemonic:
        driver.switch_to.active_element.send_keys(word) # input each mnemonic to current textbox
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
    time.sleep(0.5)
    click(driver, "/html/body/div/div[1]/div/div[2]/div[2]/div[5]/div[2]/div") # continue
    click(driver, "/html/body/div/div[1]/div/div[2]/div[2]/div[10]/div[2]/div") # continue
    time.sleep(1)
    # time.sleep(3)
    # click(driver, "/html/body/div/div[1]/div/div[2]/div[2]/div/div/div[3]/div[2]/label/span[1]/input")
    # time.sleep(0.5)
    # click(driver, "/html/body/div/div[1]/div/div[2]/div[2]/div/div/div[3]/div[4]/label/span[1]/input")
    # time.sleep(0.5)
    # click(driver, "/html/body/div/div[1]/div/div[2]/div[2]/div/div/div[4]/div") # OK
    logger.info("import unisat successufully")
    return True

def keplr_import(driver, user, option):
    password = option["password"]
    dym = user["dym"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("chrome-extension://dmkamcknogkgcdfhhbddcghachkejeap/register.html#")
    click(driver, "/html/body/div/div/div[2]/div/div/div/div/div/div[3]/div[3]/button")
    click(driver, "/html/body/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[5]/button")
    time.sleep(1)
    for word in dym:
        driver.switch_to.active_element.send_keys(word) # input each mnemonic to current textbox
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
        time.sleep(0.1)
    click(driver, "/html/body/div/div/div[2]/div/div/div[3]/div/div/form/div[6]/div/button")
    input_content(driver, "/html/body/div/div/div[2]/div/div/div[4]/div/div/form/div/div[1]/div[2]/div/div/input", "DYM")
    input_content(driver, "/html/body/div/div/div[2]/div/div/div[4]/div/div/form/div/div[3]/div[2]/div/div/input", password)
    input_content(driver, "/html/body/div/div/div[2]/div/div/div[4]/div/div/form/div/div[5]/div[2]/div/div/input", password)
    click(driver, "/html/body/div/div/div[2]/div/div/div[4]/div/div/form/div/div[7]/button")
    time.sleep(5)
    input_content(driver, "/html/body/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/div[2]/input", "dym")
    click(driver, "/html/body/div/div/div[2]/div/div/div/div/div/div[5]/div[1]/div[2]/div/div/div")
    click(driver, "/html/body/div/div/div[2]/div/div/div/div/div/div[9]/div/button")
    time.sleep(0.5)
    logger.info("import dym successfully")

def okx_wallet_import(driver, user, option):
    password = option["password"]
    mnemonic = user["mnemonic"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("chrome-extension://mcohilncbfahbmgdjkbpemcciiolgcge/home.html#initialize")
    click(driver, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/button") # import
    click(driver, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[1]") # import key
    time.sleep(1)
    for word in mnemonic:
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
        driver.switch_to.active_element.send_keys(word) # input each mnemonic to current textbox
    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
    click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div/button")
    input_content(driver, "/html/body/div[1]/div/div/div/div[2]/form/div[1]/div[2]/div/div/div/div/input", password)
    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
    input_content(driver, "/html/body/div[1]/div/div/div/div[2]/form/div[3]/div[2]/div/div/div/div/input", password)
    click(driver, "/html/body/div[1]/div/div/div/div[2]/form/div[5]/div/div[2]/div/div/div/button") # confirm
    time.sleep(4)
    driver.get("chrome-extension://mcohilncbfahbmgdjkbpemcciiolgcge/home.html")
    time.sleep(2)
    # add sBTC
    # driver.get("chrome-extension://mcohilncbfahbmgdjkbpemcciiolgcge/home.html#manage-coin")
    # input_content(driver, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/input[2]", "sBTC")
    # click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[3]")
    # time.sleep(2)

    # driver.get("chrome-extension://mcohilncbfahbmgdjkbpemcciiolgcge/home.html#coin?coinId=22900")
    # click(driver, "/html/body/div[1]/div/div/div/div[1]/div/div/div[3]/div")
    # click(driver, "/html/body/div[1]/div/div/div[3]/div/div[3]/div/div/div[2]/div/div[4]")
    # click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[3]/div[3]/i")
    # logger.debug(user["name"])
    # clipboard_content = pyperclip.paste()
    # logger.debug(clipboard_content)
    print("import okx wallet success for {}".format(user["acc_id"]))
    return True

def sub_wallet_import(driver, user, option):
    password = option["password"]
    mnemonic = user["mnemonic"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("chrome-extension://onhogfjeacnfoofkfgppdlbmlmnplgbn/index.html#/welcome")
    click(driver, "/html/body/div/div[3]/div[1]/div[2]/div[2]/div[3]/button[2]") # import
    click(driver, "/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/button") # scroll down
    time.sleep(2)
    click(driver, "/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/label/span[2]")
    click(driver, "/html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/button") # Continue
    click(driver, "/html/body/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div")
    click(driver, "/html/body/div/div[2]/div[3]/div[2]/div/div[2]/div[2]/div/button")
    input_content(driver, "/html/body/div/div[3]/div[1]/div/div[2]/div/form/div[1]/div/div/div/div/div/div/span/input", password)
    input_content(driver, "/html/body/div/div[3]/div[1]/div/div[2]/div/form/div[2]/div/div/div/div/div/div/span/input", password)
    click(driver, "/html/body/div/div[3]/div[1]/div/div[2]/div/form/div[4]/div/div/div[1]/div/label/span[2]")
    click(driver, "/html/body/div/div[3]/div[1]/div/div[3]/div/button")
    time.sleep(1)
    for word in mnemonic:
        driver.switch_to.active_element.send_keys(word) # input each mnemonic to current textbox
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
        time.sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
    click(driver, "/html/body/div/div[3]/div[1]/div/div[3]/div/button")
    click(driver, "/html/body/div/div[3]/div[1]/div[3]/div/button") # confirm
    click(driver, "/html/body/div/div[2]/div[3]/div[2]/div/div[2]/div[3]/div/button[1]")
    return True