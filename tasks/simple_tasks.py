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
#### import twitter auth token

def open_edit_cookie_and_swith(driver):
    # get the extension box
    extn = pyautogui.locateOnScreen(os.path.join('.', 'icons', "edit_cookie.png"))
    # click on extension 
    pyautogui.click(x=extn[0],y=extn[1],clicks=1,interval=0.0,button="left")
    time.sleep(1)
    window_handles = driver.window_handles
    for handle in window_handles:
        # 切换到新窗口
        driver.switch_to.window(handle)
        
        # 如果确认是扩展窗口，则进行你需要的操作
        if "EditCookie" in driver.title:
            # 这里执行你想做的操作
            break

def switch_to_twitter(driver):
    window_handles = driver.window_handles
    for handle in window_handles:
        # 切换到新窗口
        driver.switch_to.window(handle)
        
        # 如果确认是扩展窗口，则进行你需要的操作
        if "twitter" in driver.current_url:
            # 这里执行你想做的操作
            break

def import_twitter(driver, user, option):
    token = user['twitter'].split("----")[2].rstrip()
    handler = driver.current_window_handle
    driver.switch_to.window(handler)
    driver.get("https://twitter.com/")
    open_edit_cookie_and_swith(driver)
    click(driver, '/html/body/div[1]/nav/div/div/button') # click add cookie
    input_content(driver, "/html/body/form[2]/div[2]/input", "auth_token")
    input_content(driver, "/html/body/form[2]/div[3]/textarea", token)
    click(driver, '/html/body/form[2]/div[5]/button') # click add cookie
    switch_to_twitter(driver)
    driver.refresh()
    time.sleep(5)
    return True

#### import discord token
def open_discord_login_and_swith(driver):
    # get the extension box
    extn = pyautogui.locateOnScreen(os.path.join('.', 'icons', "discord_login.png"))
    # click on extension 
    pyautogui.click(x=extn[0],y=extn[1],clicks=1,interval=0.0,button="left")
    time.sleep(1)
    window_handles = driver.window_handles
    for handle in window_handles:
        # 切换到新窗口
        driver.switch_to.window(handle)
        logger.debug(driver.title)
        # 如果确认是扩展窗口，则进行你需要的操作
        if "Discord Token" in driver.title:
            # 这里执行你想做的操作
            break

def swith_to_discord(driver):
    window_handles = driver.window_handles
    for handle in window_handles:
        # 切换到新窗口
        driver.switch_to.window(handle)
        
        # 如果确认是扩展窗口，则进行你需要的操作
        if "discord" in driver.current_url:
            # 这里执行你想做的操作
            break

def import_discord(driver, user, option):
    token = user['discord'].split("---")[-1].rstrip()
    handler = driver.current_window_handle
    driver.switch_to.window(handler)
    driver.get("https://discord.com/login")
    open_discord_login_and_swith(driver)
    input_content(driver, "/html/body/div/div/div/input", token)
    click(driver, '/html/body/div/div/div/button') # click add cookie
    swith_to_discord(driver)
    return True

#### follow twitter users

def follow_user(driver, to_follow):
    driver.get("https://twitter.com/"+to_follow)
    # Wait for the follow button to be clickable and then click it
    click(driver, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/div/div/span/span")
    time.sleep(1)

def follow_users(driver, user, option):
    following = option["following"]
    for to_follow in following:
        follow_user(driver, to_follow)
    logger.info("follow twitter is success for {}".format(user["acc_id"]))
    return True

#### test daily check
def test_daily(driver, _user, _option):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://www.google.com")
    time.sleep(0.5)
    return True

def nfp_daily_check(driver, _user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://nfprompt.io/earn?invitecode=1bX2Jmzj")
    if check_element_content(driver, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/span", ":", 5):
        logger.info("nfp daily True")
        return True
    if check_element_content(driver, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/button/span", "Claim", 5):
        driver.get("https://nfprompt.io/earn?invitecode=1bX2Jmzj")
    click(driver, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/button/span")
    click(driver, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[1]/span")
    time.sleep(2)
    ### tricky solution for wallet connect
    driver.execute_script(
    """document.querySelector('w3m-modal').shadowRoot.querySelector('wui-flex > wui-card > w3m-router').shadowRoot.querySelector('div > w3m-connect-view').shadowRoot.querySelector('wui-flex > wui-list-wallet:nth-child(4)').shadowRoot.querySelector('button').click();""")
    switch_to_okwallet(driver)
    input_password_and_unlock_okxwallet(driver, password)
    okxwallet_click(driver,
                    ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                     "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                     "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
                    30)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    if check_element_content(driver, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/span", ":", 5):
        logger.info("nfp daily True")
        return True
    click(driver, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/button/span")
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
    result = check_element_content(driver, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/span", ":", 30)
    logger.info("nfp daily {}".format(result))
    return True

def ultiverse_daily_explore(driver, _user, option):
    option["network_id"] = "204"
    switch_to_network(driver, _user, option)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://pilot.ultiverse.io")
    time.sleep(5)
    logger.debug("open the page")
    if check_element_content(driver, "/html/body/div[1]/div/div[1]/div/div/div/div[1]/div/div[3]/div/button", "Connect", 3):
        logger.debug("try to connect and click")
        click(driver, "/html/body/div[1]/div/div[1]/div/div/div/div[1]/div/div[3]/div/button")
        time.sleep(1)
        try:
            click(driver, "/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/img[3]")
            time.sleep(1)
        except:
            pass
        # switch_to_okwallet(driver)
        # input_password_and_unlock(driver, password)
        time.sleep(1)
        okx_wallet_confirm(driver)
        time.sleep(3)
    try:
        okx_wallet_confirm(driver)
    except:
        pass
    # if check_element_content(driver, "/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div[2]/div[5]/button", "Join", 5):
    # 使用JavaScript来模拟点击
    x_coordinate = 10  # 替换为你想点击的X坐标
    y_coordinate = 10  # 替换为你想点击的Y坐标
    script = f"document.elementFromPoint({x_coordinate}, {y_coordinate}).click();"
    driver.execute_script(script)
    time.sleep(1)
    # 使用JavaScript来模拟点击
    x_coordinate = 10  # 替换为你想点击的X坐标
    y_coordinate = 10  # 替换为你想点击的Y坐标
    script = f"document.elementFromPoint({x_coordinate}, {y_coordinate}).click();"
    driver.execute_script(script)
    time.sleep(0.5)
    time.sleep(1)
    try:
        if check_element_content(driver, "/html/body/div[1]/div/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div[5]/div[2]/button", "exploring", 5):
            logger.info("ultiverse daily explore {}".format("True"))
            return True
    except:
        pass

    explore_count = 0
    try:
        soul_number = fetch_content(driver, "/html/body/div[1]/div/div[1]/div/header/div/div[2]/div[2]/div[2]/div/p[1]/span[2]")
        explore_count = int(int(soul_number)/50)
    except:
        pass
    time.sleep(1)
    logger.debug("explore_count is {}".format(explore_count))
    click(driver, "/html/body/div[1]/div/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div[5]/div[2]/button")
    # for i in range(min(explore_count, 5)):
    #     click(driver, "/html/body/div[1]/div/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div[{}]/div[5]/div[2]/button".format(str(i+1)))
    #     time.sleep(0.5)
    time.sleep(1)
    click(driver, "/html/body/div[1]/div/div[1]/div/div/div[1]/div/div[2]/div/div[3]/div/div[2]/button")
    click(driver, "/html/body/div[3]/div/div/div[3]/button")
    okxwallet_click(driver,
                ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                    "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                    "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                    "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                    "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                ],
                30)
    result = check_element_content(driver, "/html/body/div[1]/div/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div[109]/div/div[3]/button", "Close", 50)
    if result:
        click(driver, "/html/body/div[1]/div/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div[109]/div/div[3]/button")
        logger.info("ultiverse daily explore {}".format(result))
        return True
    return False
# chrome-extension://nebnhfamliijlghikdgcigoebonmoibm/fullpage.html#/ aleo wallet

def google_login(driver, user, option):
    google_accounts = user["google_account"].split("----")
    email = google_accounts[0]
    password = google_accounts[1]
    recover_email = google_accounts[2]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://www.google.com/")
    click(driver, "/html/body/div[1]/div[1]/div/div/div/div/div[2]/a")
    input_content(driver, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input", email)
    click(driver, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span")
    input_content(driver, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input", password)
    click(driver, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span")
    result = check_element_content(driver, "/html/body/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/div/a", "", 60)
    logger.info("google login is {} for {}".format(result, user["acc_id"]))
    return result

def transfer_eth_to_ok_coin(_driver, user, _option):
    w3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth'))
    gas_price_limit = w3.to_wei(25, "gwei")
    while(w3.eth.gas_price > gas_price_limit):
        time.sleep(60)
        logger.info("Too expensive, wait for a while")
    
    lower = 0.015
    upper = 0.02
    left_amount = 0.025
    amount = round(random.uniform(lower, upper), 8)
    value = w3.to_wei(amount, 'ether')
    w3.eth.account.enable_unaudited_hdwallet_features()
    account = w3.eth.account.from_mnemonic(" ".join(user["mnemonic"]), account_path="m/44'/60'/0'/0/0")
    to_addr = w3.to_checksum_address(user["ok_addr"])

    balance = w3.eth.get_balance(account.address)
    if balance < value + w3.to_wei(left_amount, 'ether'):
        logger.info("Not enough eth in {} and skip it".format(user["acc_id"]))
        return True

    logger.info("transfer {} eth from {} to {} for {}".format(amount, account.address, to_addr, user["acc_id"]))
    w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
    tx_hash = w3.eth.send_transaction({
        "from": account.address,
        "to": to_addr,
        "value": value
    })
    logger.info(f"Transaction sent with hash: {tx_hash.hex()}")