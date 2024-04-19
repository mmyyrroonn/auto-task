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
click, fetch_attribute,
fetch_content,input_content,
clear_windows_and_resize,switch_to_metamask,
check_element_content,input_password_and_unlock,
metamask_click, switch_to_network, switch_to_page, click_white_space,
switch_to_okwallet, input_password_and_unlock_okxwallet, okxwallet_click, okx_connect_and_switch_network)

def era_land_eth(driver, user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    network = "zkSync"
    okx_connect_and_switch_network(driver, password, network)
    driver.get("https://app.eralend.com/")
    try:
        okxwallet_click(driver,
                        ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                        "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                                ],
                        30)
        logger.debug("auto login")
    except:
        logger.debug("No auto login")
        pass

    while True: 
        if check_element_content(driver, "/html/body/div/div[1]/div[1]/div[1]/div[1]", "Market", 20):
            break
    if check_element_content(driver, "/html/body/div/header/div/div/div[2]/div/div[1]/button", "Connect", 5):
        logger.debug("Manual connect")
        click(driver, "/html/body/div/header/div/div/div[2]/div/div[1]/button")
        time.sleep(2)
        driver.execute_script(
        """document.querySelector('onboard-v2').shadowRoot.querySelector('section').querySelector('div').querySelector('div').querySelector('div').querySelector('div').querySelector('div').querySelector('div').querySelector('div.content.flex.flex-column.svelte-1qwmck3').querySelector('div.scroll-container.svelte-1qwmck3').querySelector('div.container.flex.items-center.svelte-tz7ru1').querySelector('label').querySelector('span').click();""")
        time.sleep(1)
        driver.execute_script(
        """document.querySelector('onboard-v2').shadowRoot.querySelector('section > div > div > div > div > div > div > div.content.flex.flex-column.svelte-1qwmck3 > div.scroll-container.svelte-1qwmck3 > div.svelte-1qwmck3 > div > div > div:nth-child(3) > button').click();""")
        okxwallet_click(driver,
                        ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                        "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                                ],
                        30)
    try:
        click(driver, "/html/body/div/header/div/div/div[2]/div/div[2]/li") # wrong network
        click(driver, "/html/body/div[2]/div[3]/ul/li[1]/span[1]")
    except:
        logger.debug("No wrong network")
        pass
    driver.get("https://app.eralend.com/")
    while True: 
        if check_element_content(driver, "/html/body/div/div[1]/div[1]/div[1]/div[1]", "Market", 20):
            break
    click(driver, "/html/body/div/div[1]/div[2]/div[3]/div[2]/div[8]/button") # Manage
    click(driver, "/html/body/div[2]/div[3]/div/div/div[2]/form/div/div[1]/div[1]/div[1]/p[3]") #75%
    click(driver, "/html/body/div[2]/div[3]/div/div/div[2]/form/div/button") #supply
    okxwallet_click(driver,
                        ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                        "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                                ],
                        30)
    _ = check_element_content(driver, "/html/body/div[3]/div[3]/div/div/button[2]", "Ok", 60)
    click(driver, "/html/body/div[3]/div[3]/div/div/button[2]")
    logger.debug("supply success")
    driver.get("https://app.eralend.com/")
    while True: 
        if check_element_content(driver, "/html/body/div/div[1]/div[1]/div[1]/div[1]", "Market", 20):
            break
    click(driver, "/html/body/div/div[1]/div[2]/div[3]/div[2]/div[8]/button") # Manage
    click(driver, "/html/body/div[2]/div[3]/div/div/div[1]/div/div/button[2]")
    click(driver, "/html/body/div[2]/div[3]/div/div/div[3]/form/div/div/div[1]/p[1]") #MAX
    click(driver, "/html/body/div[2]/div[3]/div/div/div[3]/form/div/button") #supply
    okxwallet_click(driver,
                        ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                        "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                                ],
                        30)
    result = check_element_content(driver, "/html/body/div[3]/div[3]/div/div/button[2]", "Ok", 60)
    logger.info("era land is {} for {}".format(result, user['acc_id']))
    return result

def okx_wallet_exchange(driver, user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    network = "zkSync"
    okx_connect_and_switch_network(driver, password, network)
    driver.get("chrome-extension://mcohilncbfahbmgdjkbpemcciiolgcge/home.html#network-management?tab=0")
    input_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/input[2]", "Zksync")
    time.sleep(1)
    click(driver, "/html/body/div[1]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]")
    click(driver, "/html/body/div[1]/div/div/div/div[3]/div[3]/div[1]") # Swap Page
    ### try to sell eth
    click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/span/span[1]")
    input_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/input[2]", "era_eth")
    time.sleep(2)
    click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[4]/div/div/div/div/div")
    coins = ['usdc', 'usdt']
    random.shuffle(coins)
    amount = float(fetch_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div/div"))
    logger.debug("{} eth".format(amount))
    if amount > 0.01:
        logger.debug("Has enough eth to sell")
        gas_amount = round(random.uniform(0.001, 0.003), 6)
        logger.debug("{} gas amount".format(gas_amount))
        value_amount = round(amount - gas_amount, 5)
        logger.debug("{} value amount".format(value_amount))
        input_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/input[2]", value_amount)
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/span/span[1]")
        try:
            click(driver, "/html/body/div[4]/div[2]/div/div[1]/i")
        except:
            pass
        input_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/input[2]", coins[0])
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div[1]/div")
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/button")
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div/button")

        _ = check_element_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/button/span", "Do", 30)
        # buy eth back
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/button")
        time.sleep(3)
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div/span")
        time.sleep(3)
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/span[2]/span") # MAx
        time.sleep(3)
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/button")

        _ = check_element_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/button", "Swap", 30)
        time.sleep(1)
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/button")
        time.sleep(1)
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div/button")
        result = check_element_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div", "Complete", 30)
        logger.info("okx_wallet_exchange is {} for {}".format(result, user['acc_id']))
        return result
    else:
        # try to buy eth directly through usdt
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/span/span[1]")
        input_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/input[2]", coins[0])
        time.sleep(1)
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div[1]/div/div[1]/div[2]/div[1]")

        if check_element_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div/div", "0", 5):
            click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/span/span[1]")
            input_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/input[2]", coins[1])
            time.sleep(1)
            click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div[1]/div/div[1]/div[2]/div[1]")
        
        if check_element_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div/div", "0", 5):
            logger.info("Not usdc or usdt to buy, okx_wallet_exchange is False for {}".format(user['acc_id']))
            return False

        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/span/span[1]")
        try:
            click(driver, "/html/body/div[4]/div[2]/div/div[1]/i")
        except:
            pass
        input_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/input[2]", "era_eth")
        time.sleep(1)
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div[1]/div")
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/span[2]/span") # MAx
        time.sleep(2)
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/button")

        _ = check_element_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/button", "Swap", 30)
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/button")
        time.sleep(1)
        click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div/button")
        result = check_element_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/div[1]/div", "Complete", 30)
        logger.info("okx_wallet_exchange is {} for {}".format(result, user['acc_id']))
        return result

def mav_exchange(driver, user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    network = "zkSync"
    okx_connect_and_switch_network(driver, password, network)
    driver.get("https://app.mav.xyz/?chain=324")
    try:
        okxwallet_click(driver,
                        ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                        "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                                ],
                        30)
        logger.debug("auto login")
    except:
        logger.debug("No auto login")
        pass
    if check_element_content(driver, "/html/body/div/div/header[2]/div/div/div/div[2]/div[2]/button/p", "Connect", 5):
        click(driver, "/html/body/div/div/header[2]/div/div/div/div[2]/div[2]/button") # Connect
        driver.execute_script(
            """document.querySelector('body > onboard-v2').shadowRoot.querySelector('section > div > div > div > div > div > div > div.content.flex.flex-column.svelte-ro440k > div.scroll-container.svelte-ro440k > div.container.flex.items-center.svelte-wp0cfb > label').click();""")
        time.sleep(1)
        driver.execute_script(
            """document.querySelector('body > onboard-v2').shadowRoot.querySelector('section > div > div > div > div > div > div > div.content.flex.flex-column.svelte-ro440k > div.scroll-container.svelte-ro440k > div.svelte-ro440k > div > div > button:nth-child(2)').click();""")
        okxwallet_click(driver,
                        ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                        "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                                ],
                        30)
        logger.debug("connect")
    driver.get("https://app.mav.xyz/?chain=1")
    click(driver, "/html/body/div/div/header[2]/div/div/div/div[2]/div[3]/div") # network
    click(driver, "/html/body/div[2]/div[3]/ul/li[3]") # zksync
    time.sleep(5)
    usdt_address = "0x493257fd37edb34451f62edf8d2a0c418852ba4c"
    usdc_address = "0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4"
    ### try to sell eth
    coins = [usdt_address, usdc_address]
    random.shuffle(coins)
    driver.get("https://app.mav.xyz/?chain=324"+"&tokenA=ETH&tokenB="+coins[0])
    _ = check_element_content(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/button/h6/div/h6", "ETH", 10)
    time.sleep(5)
    amount = float(fetch_attribute(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div/p/span", "aria-label"))
    logger.debug("{} eth".format(amount))
    if amount > 0.01:
        logger.debug("Has enough eth to sell")
        gas_amount = round(random.uniform(0.001, 0.002), 6)
        logger.debug("{} gas amount".format(gas_amount))
        value_amount = round(amount - gas_amount, 5)
        logger.debug("{} value amount".format(value_amount))
        input_content(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/input", value_amount)
        _ = check_element_content(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/button", "Swap", 20)
        click(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/button")
        time.sleep(1)
        click(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/button")
        okxwallet_click(driver,
                        ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                        "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                                ],
                        30)
        
        _ = check_element_content(driver, "/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div/button[1]", "Done", 60)

        # buy eth back
        driver.get("https://app.mav.xyz/?chain=324"+"&tokenA="+coins[0]+"&tokenB=ETH")
        time.sleep(10)
        click(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div") # Max
        _ = check_element_content(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/button", "Swap", 20)
        click(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/button")
        time.sleep(1)
        if check_element_content(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/button", "Approve", 5):
            click(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/button")
            okxwallet_click(driver,
                        ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                        "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                                ],
                        30)
        _ = check_element_content(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/button", "Confirm", 60)
        click(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/button")
        okxwallet_click(driver,
                        ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                        "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                                ],
                        30)
        
        result = check_element_content(driver, "/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div/button[1]", "Done", 30)
        logger.info("mav exchange is {} for {}".format(result, user['acc_id']))
        return result
    else:
        # buy eth back
        driver.get("https://app.mav.xyz/?chain=324"+"&tokenA="+coins[0]+"&tokenB=ETH")
        time.sleep(10)
        if check_element_content(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div/p", "-", 2):
            driver.get("https://app.mav.xyz/?chain=324"+"&tokenA="+coins[1]+"&tokenB=ETH")
            time.sleep(10)
        if check_element_content(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div/p", "-", 2):
            logger.info("Not usdc or usdt to buy, max exchange is False for {}".format(user['acc_id']))
            return False
        click(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div") # Max
        _ = check_element_content(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/button", "Swap", 20)
        click(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/button")
        time.sleep(1)
        if check_element_content(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/button", "Approve", 5):
            click(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/button")
            okxwallet_click(driver,
                        ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                        "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                                ],
                        30)
        _ = check_element_content(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/button", "Confirm", 60)
        click(driver, "/html/body/div[1]/div/div/div/div/div[1]/div[2]/div/button")
        okxwallet_click(driver,
                        ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                        "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                        "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                                ],
                        30)
        
        result = check_element_content(driver, "/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div/button[1]", "Done", 60)
        logger.info("mav exchange is {} for {}".format(result, user['acc_id']))
        return result

def tevaera_nft_mint(driver, user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    network = "zkSync"
    okx_connect_and_switch_network(driver, password, network)
    driver.get("https://tevaera.com/login")
    if check_element_content(driver, "/html/body/div/div/div/div/div[1]/section/div[1]/h3/span[1]", "Welcome", 5):
        logger.info("tevaera_nft_mint is {} for {}".format(True, user['acc_id']))
        return True
    if check_element_content(driver, "/html/body/div[3]/div/div/div[2]/div/div/div/button[1]", "Login", 5):
        click(driver, "/html/body/div[3]/div/div/div[1]/button")
    click(driver, "/html/body/div/div/div/section[2]/div[1]/div[3]/button[3]")
    try:
        okxwallet_click(driver,
                ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                        ],
                30)
    except:
        pass
    if check_element_content(driver, "/html/body/div[3]/div/div/div[2]/div/div/div/button[1]", "Login", 5):
        click(driver, "/html/body/div[3]/div/div/div[1]/button")
    click(driver, "/html/body/div/div/div/section[2]/div[1]/div[3]/button[3]")
    click(driver, "/html/body/div[3]/div/div/div[2]/div/div/div/button[1]")
    time.sleep(5)
    okxwallet_click(driver,
                ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                        ],
                30)
    if check_element_content(driver, "/html/body/div/div/div/div/div[1]/section/div[1]/h3/span[1]", "Welcome", 5):
        logger.info("tevaera_nft_mint is {} for {}".format(True, user['acc_id']))
        return True
    if check_element_content(driver, "/html/body/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/button", "Mint", 10):
        click(driver, "/html/body/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/button")
        okxwallet_click(driver,
                ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                        ],
                30)
        _ = check_element_content(driver, "/html/body/div[3]/div/div/div[2]/div/div[2]/a/button", "Ok", 60)
        click(driver, "/html/body/div[3]/div/div/div[2]/div/div[2]/a/button")
        if check_element_content(driver, "/html/body/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/h2", "Guardian", 30):
            click(driver, "/html/body/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/a")
        result = check_element_content(driver, "/html/body/div/div/div/div/div/div[2]/div[1]/div[1]/div/section/div/div/div[1]/div/div/div[2]/div/div[1]/div/div/div[1]/h2", "Welcome", 10)
        logger.info("tevaera_nft_mint is {} for {}".format(result, user['acc_id']))
        return result
    
def dmail_send_message(driver, user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    network = "zkSync"
    okx_connect_and_switch_network(driver, password, network)
    driver.get("https://mail.dmail.ai/inbox")
    if check_element_content(driver, "/html/body/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[1]/span", "MetaMask", 10):
        click(driver, "/html/body/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[1]")
        okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
    if check_element_content(driver, "/html/body/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[1]/span", "MetaMask", 5):
        click(driver, "/html/body/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[1]")
        okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
    if check_element_content(driver, "/html/body/div[1]/div/div[2]/div[3]/div/div/div[4]/a", "Next step", 5):
        click(driver, "/html/body/div[1]/div/div[2]/div[3]/div/div/div[4]/a")
        time.sleep(1)
        click(driver, "/html/body/div[1]/div/div[2]/div[3]/div/div/div[4]/a")
        time.sleep(1)
        click(driver, "/html/body/div[1]/div/div[2]/div[3]/div/div/div[4]/a")
    click(driver, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[1]/div") # Compose
    for i in range(5):
        click_white_space(driver)
    input_content(driver, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/input", "dmailcs@dmail.ai")
    input_content(driver, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[3]/div/input", "qrr7b-qjo44-j4ojq-ckxgd-uht7s-u6kif-mmult-v36gz-klkor-smsil-2ae")
    email_subjects = [
        "Quarterly Financial Overview",
        "Upcoming Team Building Event",
        "New Office Opening Announcement",
        "Important Security Update Required",
        "Client Feedback Collection",
        "Annual Company Retreat Planning",
        "Software Version Upgrade",
        "Staff Training Session Schedule",
        "Reminder: Project Deadline Approaching",
        "Invitation to Webinar on Market Trends",
        "Please review the attached financial report for this quarter and provide your feedback.",
        "Join us for an exciting team building event next Friday to strengthen our collaboration.",
        "We are excited to announce the opening of our new office in downtown next month!",
        "A critical security update is now available and must be applied to all company devices by EOD.",
        "We are gathering client feedback; please ensure your clients complete the survey by Wednesday.",
        "Your ideas for the annual company retreat are welcome; please submit them by next meeting.",
        "The latest software update brings many improvements and will be deployed next Tuesday.",
        "The upcoming staff training sessions are mandatory; find the schedule attached.",
        "This is a reminder that the project deadline is just one week away, please prioritize accordingly.",
        "You're invited to a webinar on the latest market trends; secure your spot today!"
    ]
    random.shuffle(email_subjects)
    input_content(driver, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[4]/div[1]/input", email_subjects[0])

    if not check_element_content(driver, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[3]/div[2]/div/div/span", "zkSync", 5):
        click(driver, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[3]/div[2]/div/div/span")
        click(driver, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[3]/div[2]/div/ul/li[3]")
    click(driver, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/a[1]")
    okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
    result = check_element_content(driver, "/html/body/div[1]/div/div[2]/div[1]/div[1]", "Sent", 60)
    logger.info("dmail sent is {} for {}".format(result, user['acc_id']))
    return result

def odos_exchange(driver, user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    network = "zkSync"
    okx_connect_and_switch_network(driver, password, network)
    driver.get("https://app.odos.xyz/")
    if check_element_content(driver, "/html/body/div/div/header/div/nav/div[1]/div/div[2]/div[2]/div/button", "Connect", 10):
        click(driver, "/html/body/div/div/header/div/nav/div[1]/div/div[2]/div[2]/div/button")
        click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[4]/div/div/div/div[3]/div/div[1]/button")
        okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
    if not check_element_content(driver, "/html/body/div/div/header/div/nav/div[1]/div/div[2]/div[1]/div/div/button/div[1]/div[2]/span", "zkSync", 10):
        click(driver, "/html/body/div/div/header/div/nav/div[1]/div/div[2]/div[1]/div/div/button")
        click(driver, "/html/body/div/div/header/div/nav/div[1]/div/div[2]/div[1]/div/div/div/ul/li[6]")
    # try to sell eth
    time.sleep(5)
    if not check_element_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[1]/button/span", "ETH", 10):
        click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[1]/button")
        input_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div/input", "ETH")
        time.sleep(2)
        click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div/div[3]/div[1]/button")
    coins = ['USDC.e', 'USDT']
    random.shuffle(coins)
    amount = float(fetch_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]").split(':')[1])
    logger.debug("{} eth".format(amount))
    if amount > 0.01:
        logger.debug("Has enough eth to sell")
        gas_amount = round(random.uniform(0.001, 0.003), 6)
        logger.debug("{} gas amount".format(gas_amount))
        value_amount = round(amount - gas_amount, 5)
        logger.debug("{} value amount".format(value_amount))
        input_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[2]/input", value_amount)
        if not check_element_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div/div/div[1]/div[1]/button/span", coins[0], 5):
            click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div/div/div[1]/div[1]/button")
            input_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div/input", coins[0])
            time.sleep(2)
            click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div/div[3]/div[1]/button")
        if check_element_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[2]/div/button/div/span", "Refresh", 5):
            click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[2]/div/button")

        if check_element_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[2]/div/button/div/span", "Swap", 5):
            click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[2]/div/button")
            okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
        
        _ = check_element_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div/div[2]/span", "Completed", 60)
        click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div/div[5]/button") # Return to swap

        time.sleep(3)
        click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div[4]/button") # Switch
        time.sleep(3)
        click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/button") # MAX
        time.sleep(3)
        if check_element_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[2]/div/button/div/span", "Approve", 10):
            click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[2]/div/button")
            okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
        
        if check_element_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[2]/div/button/div/span", "Swap", 60):
            click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[2]/div/button")
            okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
        result = check_element_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div/div[2]/span", "Completed", 60)
        logger.info("odos exchange is {} for {}".format(result, user['acc_id']))
        return result
    else:
        click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[1]/button")
        input_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div/input", coins[0])
        time.sleep(2)
        click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div/div[3]/div[1]/button")
        time.sleep(5)
        amount = float(fetch_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]").split(':')[1])
        if amount < 0.01:
            click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[1]/button")
            input_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div/input", coins[1])
            time.sleep(2)
            click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div/div[3]/div[1]/button")
        time.sleep(5)
        amount = float(fetch_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]").split(':')[1])
        if amount < 0.01:
            logger.info("Not usdc or usdt to buy, odos exchange is False for {}".format(user['acc_id']))
            return False
        if not check_element_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div/div/div[1]/div[1]/button/span", "ETH", 5):
            click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div/div/div[1]/div[1]/button")
            input_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div/input", "ETH")
            time.sleep(2)
            click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div/div[3]/div[1]/button")
        click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/button") # MAX
        time.sleep(3)
        if check_element_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[2]/div/button/div/span", "Refresh", 5):
            click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[2]/div/button")
        if check_element_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[2]/div/button/div/span", "Approve", 10):
            click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[2]/div/button")
            okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
        
        if check_element_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[2]/div/button/div/span", "Swap", 60):
            click(driver, "/html/body/div/div/main/div/div/div[1]/div/div[2]/div/button")
            okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
        result = check_element_content(driver, "/html/body/div/div/main/div/div/div[1]/div/div[1]/div/div[2]/span", "Completed", 60)
        logger.info("odos exchange is {} for {}".format(result, user['acc_id']))
        return result

def izumi_swap(driver, user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    network = "zkSync"
    okx_connect_and_switch_network(driver, password, network)
    driver.get("https://izumi.finance/trade/swap")
    try:
        okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
    except:
        pass
    if check_element_content(driver, "/html/body/div[1]/div/div/div[4]/div[2]/div/div[1]/button", "Remove", 5):
        click(driver, "/html/body/div[1]/div/div/div[4]/div[1]/img")
    if not check_element_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[5]/div/div/div/button/span[2]", "zkSync", 5):
        click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[5]/div/div/div/button")
        time.sleep(1)
        click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[5]/div/div/div/div/div/div[1]/button[1]")
    # try to sell eth
    click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/div")
    input_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div[1]/div[1]/input", "ETH")
    time.sleep(2)
    click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div")
    coins = ['USDC.e', 'USDT']
    random.shuffle(coins)
    amount = float(fetch_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/span"))
    logger.debug("{} eth".format(amount))
    if amount > 0.01:
        logger.debug("Has enough eth to sell")
        gas_amount = round(random.uniform(0.001, 0.003), 6)
        logger.debug("{} gas amount".format(gas_amount))
        value_amount = round(amount - gas_amount, 5)
        logger.debug("{} value amount".format(value_amount))
        if not check_element_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/div/div/div/h4", coins[0], 5):
            click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/div/div")
            input_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/div[3]/div[2]/div/div[1]/div[1]/input", coins[0])
            time.sleep(2)
            click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/div[3]/div[2]/div/div[2]/div/div/div[1]/div")
        input_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/input", value_amount)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
        time.sleep(3)
        if check_element_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[6]/div[2]/button[1]", "Swap", 5):
            click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[6]/div[2]/button[1]")
            okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
        
        _ = check_element_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div/p[1]", "Swap Success", 60)
        click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div[1]/img") # Return to swap

        time.sleep(3)
        click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[3]") # Switch
        time.sleep(3)
        click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]") # MAX
        time.sleep(3)
        if check_element_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[6]/div[2]/button[2]", "Approve", 10):
            click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[6]/div[2]/button[2]")
            okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
        
        if check_element_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[6]/div[2]/button[1]", "Swap", 60):
            click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[6]/div[2]/button[1]")
            okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
        result = check_element_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div/p[1]", "Swap Success", 60)
        logger.info("izumi_swap exchange is {} for {}".format(result, user['acc_id']))
        return result
    else:
        click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/div")
        input_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div[1]/div[1]/input", coins[0])
        time.sleep(2)
        click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div")
        time.sleep(3)
        amount = float(fetch_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/span"))
        if amount < 0.01:
            click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/div")
            input_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div[1]/div[1]/input", coins[1])
            time.sleep(2)
            click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div")
        time.sleep(3)
        amount = float(fetch_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/span"))
        if amount < 0.01:
            logger.info("Not usdc or usdt to buy, izumi exchange is False for {}".format(user['acc_id']))
            return False
        if not check_element_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/div/div/div/h4", "ETH", 5):
            click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/div/div")
            input_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/div[3]/div[2]/div/div[1]/div[1]/input", "ETH")
            time.sleep(2)
            click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/div[3]/div[2]/div/div[2]/div/div/div[1]/div")
        click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]") # MAX
        time.sleep(3)
        if check_element_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[6]/div[2]/button[2]", "Approve", 10):
            click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[6]/div[2]/button[2]")
            okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
        
        if check_element_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[6]/div[2]/button[1]", "Swap", 60):
            click(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[6]/div[2]/button[1]")
            okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
        result = check_element_content(driver, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div/p[1]", "Swap Success", 60)
        logger.info("izumi_swap exchange is {} for {}".format(result, user['acc_id']))
        return result
    
def zero_land_lending(driver, user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    network = "zkSync"
    okx_connect_and_switch_network(driver, password, network)
    driver.get("https://app.zerolend.xyz/reserve-overview/?underlyingAsset=0x5aea5775959fbc2557cc8789bc1bf90a239d9a91&marketName=proto_zksync_era_v3")
    try:
        okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
    except:
        pass
    if check_element_content(driver, "/html/body/div[1]/header/button", "Connect", 5):
        click(driver, "/html/body/div[1]/header/button")
        time.sleep(2)
        click(driver, "/html/body/div[8]/div[3]/div[1]/button[3]")
        okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
    time.sleep(6)
    click(driver, "/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div/div[1]/div/button[2]")
    time.sleep(2)
    amount = float(fetch_content(driver, "/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/h4"))
    if amount < 0.001:
        logger.info("Not eth, zero land is False for {}".format(user['acc_id']))
        return False
    gas_amount = round(random.uniform(0.001, 0.003), 6)
    logger.debug("{} gas amount".format(gas_amount))
    value_amount = round(amount - gas_amount, 5)
    click(driver, "/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/button") # Supply
    input_content(driver, "/html/body/div[8]/div[3]/div[1]/div[2]/div[1]/div[1]/input", value_amount)
    click(driver, "/html/body/div[8]/div[3]/div[3]/button")
    okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
    _ = check_element_content(driver, "/html/body/div[8]/div[3]/div[1]/h2", "All done", 60)
    click(driver, "/html/body/div[8]/div[3]/div[2]/button")

    # to withdraw
    click(driver, "/html/body/div[1]/header/div[2]/ul/li[2]/a")
    click(driver, "/html/body/div[1]/main/div[2]/div/div[2]/div/div[1]/div[1]/div[3]/div[3]/div[5]/button[1]")
    if check_element_content(driver, "/html/body/div[7]/div[3]/div[1]/div[1]/div/button[2]", "Continue", 5):
        click(driver, "/html/body/div[7]/div[3]/div[1]/div[1]/div/button[2]")
    click(driver, "/html/body/div[7]/div[3]/div[1]/div[1]/div[2]/div[2]/button")
    time.sleep(5)
    if check_element_content(driver, "/html/body/div[7]/div[3]/div[1]/div[4]/button[1]/div/p", "Approve to", 5):
        click(driver, "/html/body/div[7]/div[3]/div[1]/div[4]/button[1]")
        okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)

        _ = check_element_content(driver, "/html/body/div[7]/div[3]/div[1]/div[4]/button[1]", "Approve Confirmed", 60)
        click(driver, "/html/body/div[7]/div[3]/div[1]/div[4]/button[2]")
        okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
    else:
        click(driver, "/html/body/div[7]/div[3]/div[1]/div[4]/button")
        okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
    result = check_element_content(driver, "/html/body/div[6]/div[3]/div[1]/h2", "All done", 60)
    if not result:
        # check again
        driver.get("https://app.zerolend.xyz/dashboard/")
        result = check_element_content(driver, "/html/body/div[1]/main/div[2]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/p", "Nothing supplied", 10)
    logger.info("zero lend is {} for {}".format(result, user['acc_id']))
    return result


def koi_finance(driver, user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    network = "zkSync"
    okx_connect_and_switch_network(driver, password, network)
    driver.get("https://app.koi.finance/swap")
    if check_element_content(driver, "/html/body/div/div/div/div[1]/nav/div[3]/button", "Connect", 5):
        click(driver, "/html/body/div/div/div/div[1]/nav/div[3]/button") # Connect
        driver.execute_script(
            """document.querySelector('body > w3m-modal').shadowRoot.querySelector('wui-flex > wui-card > w3m-router').shadowRoot.querySelector('div > w3m-connect-view').shadowRoot.querySelector('wui-flex > wui-list-wallet:nth-child(4)').click();""")
        time.sleep(1)
        okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
        logger.debug("connect")
    eth_address = "0x0000000000000000000000000000000000000000"
    usdt_address = "0x493257fd37edb34451f62edf8d2a0c418852ba4c"
    usdc_address = "0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4"
    ### try to sell eth
    coins = [usdt_address, usdc_address]
    random.shuffle(coins)
    driver.get("https://app.koi.finance/swap?"+"inputCurrency=" + eth_address + "&outputCurrency="+coins[0])
    _ = check_element_content(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/div/span", "ETH", 10)
    time.sleep(5)
    amount = float(fetch_content(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]").split(':')[1][:-3])
    logger.debug("{} eth".format(amount))
    if amount > 0.01:
        logger.debug("Has enough eth to sell")
        gas_amount = round(random.uniform(0.001, 0.002), 6)
        logger.debug("{} gas amount".format(gas_amount))
        value_amount = round(amount - gas_amount, 5)
        logger.debug("{} value amount".format(value_amount))
        input_content(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/input", value_amount)
        _ = check_element_content(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/button", "Swap", 20)
        click(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/button")
        okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
        
        _ = check_element_content(driver, "/html/body/div/div/div/div[4]/div[6]/div/div[2]", "confirmed", 60)

        # buy eth back
        driver.get("https://app.koi.finance/swap?"+"inputCurrency=" + coins[0] + "&outputCurrency="+eth_address)
        time.sleep(10)
        click(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/span") # Max
        if check_element_content(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/button", "Approve", 15):
            click(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/button")
            okxwallet_click(driver,
                ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                        ],
                30)
            try:
                okxwallet_click(driver,
                ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                        ],
                30)
            except:
                pass
        
            result = check_element_content(driver, "/html/body/div/div/div/div[4]/div[6]/div/div[2]", "confirmed", 60)
            logger.info("koi exchange is {} for {}".format(result, user['acc_id']))
            return result
        if check_element_content(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/button", "Swap", 15):
            click(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/button")
            okxwallet_click(driver,
                ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                        ],
                30)
        
            result = check_element_content(driver, "/html/body/div/div/div/div[4]/div[6]/div/div[2]", "confirmed", 60)
            logger.info("koi exchange is {} for {}".format(result, user['acc_id']))
            return result
    else:
        # buy eth back
        driver.get("https://app.koi.finance/swap?"+"inputCurrency=" + coins[0] + "&outputCurrency="+eth_address)
        time.sleep(10)
        
        if check_element_content(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]", "-", 3):
            driver.get("https://app.koi.finance/swap?"+"inputCurrency=" + coins[1] + "&outputCurrency="+eth_address)
            time.sleep(10)
        if check_element_content(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]", "-", 3):
            logger.info("Not usdc or usdt to buy, koi exchange is False for {}".format(user['acc_id']))
            return False
        click(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/span") # Max
        if check_element_content(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/button", "Approve", 15):
            click(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/button")
            okxwallet_click(driver,
                ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                        ],
                30)
            try:
                okxwallet_click(driver,
                ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                        ],
                30)
            except:
                pass
        
            result = check_element_content(driver, "/html/body/div/div/div/div[4]/div[6]/div/div[2]", "confirmed", 60)
            logger.info("koi exchange is {} for {}".format(result, user['acc_id']))
            return result
        if check_element_content(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/button", "Swap", 15):
            click(driver, "/html/body/div/div/div/div[3]/div/div[1]/div/button")
            okxwallet_click(driver,
                ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
                "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
                "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
                "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                        ],
                30)
        
            result = check_element_content(driver, "/html/body/div/div/div/div[4]/div[6]/div/div[2]", "confirmed", 60)
            logger.info("koi exchange is {} for {}".format(result, user['acc_id']))
            return result
        
def reactor_fusion_lending(driver, user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    network = "zkSync"
    okx_connect_and_switch_network(driver, password, network)
    driver.get("https://main.reactorfusion.xyz/")
    if check_element_content(driver, "/html/body/div[2]/div/div/div/div[2]/section/div/div/div[3]/button/div/span", "Agree", 5):
        click(driver, "/html/body/div[2]/div/div/div/div[2]/section/div/div/div[3]/button/div")
    time.sleep(2)
    if check_element_content(driver, "/html/body/div[1]/div/div[1]/div/div[3]/div[2]/div/div/button/div/span", "CONNECT", 5):
        click(driver, "/html/body/div[1]/div/div[1]/div/div[3]/div[2]/div/div/button")
        time.sleep(1)
        driver.execute_script(
            """document.querySelector('body > w3m-modal').shadowRoot.querySelector('wui-flex > wui-card > w3m-router').shadowRoot.querySelector('div > w3m-connect-view').shadowRoot.querySelector('wui-flex > wui-list-wallet:nth-child(3)').click();""")
        okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
                    ],
            30)
    if check_element_content(driver, "/html/body/div[1]/div/div[1]/div/div[3]/div[2]/div/div/div/button/div/span", "WRONG", 5):
        click(driver, "/html/body/div[1]/div/div[1]/div/div[3]/div[2]/div/div/div/button")
        driver.execute_script(
            """document.querySelector('body > w3m-modal').shadowRoot.querySelector('wui-flex > wui-card > w3m-router').shadowRoot.querySelector('div > w3m-networks-view').shadowRoot.querySelector('wui-grid > wui-card-select').click();""")
    click(driver, "/html/body/div[1]/div/div[1]/div/div[3]/div[1]/div/div[1]")
    # lend eth
    click(driver, "/html/body/div[1]/div/div[2]/main/div/div/div[3]/div[1]/div[2]/div/table/tbody/tr[1]")
    amount = float(fetch_content(driver, "/html/body/div[2]/div/div/div/div[2]/section/div/div/div[3]/div/div[1]/div[1]/div/span")[:-3])
    logger.debug("Has enough eth to sell")
    gas_amount = round(random.uniform(0.001, 0.002), 6)
    logger.debug("{} gas amount".format(gas_amount))
    value_amount = round(amount - gas_amount, 5)
    logger.debug("{} value amount".format(value_amount))
    input_content(driver, "/html/body/div[2]/div/div/div/div[2]/section/div/div/div[3]/div/div[1]/div[2]/input", value_amount)
    click(driver, "/html/body/div[2]/div/div/div/div[2]/section/div/div/div[3]/div/button")
    okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm with gas change
                    ],
            30)
    _ = check_element_content(driver, "/html/body/div[2]/div/div/div/div[2]/section/div/div/div[2]/div[2]", "Pending", 30)
    click(driver, "/html/body/div[2]/div/div/div/div[2]/section/div/div/div[1]/img")
    driver.get("https://main.reactorfusion.xyz/")
    click(driver, "/html/body/div[1]/div/div[2]/main/div/div/div[3]/div[1]/div[2]/div/table/tbody/tr[1]")
    click(driver, "/html/body/div[2]/div/div/div/div[2]/section/div/div/div[2]/div/div[2]")
    amount = float(fetch_content(driver, "/html/body/div[2]/div/div/div/div[2]/section/div/div/div[3]/div/div[1]/div[1]/div/span")[:-3])
    input_content(driver, "/html/body/div[2]/div/div/div/div[2]/section/div/div/div[3]/div/div[1]/div[2]/input", amount)
    click(driver, "/html/body/div[2]/div/div/div/div[2]/section/div/div/div[3]/div/button")
    okxwallet_click(driver,
            ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
            "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
            "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm with gas change
                    ],
            30)
    result = check_element_content(driver, "/html/body/div[2]/div/div/div/div[2]/section/div/div/div[2]/div[2]", "Pending", 30)
    logger.info("reactor_fusion_lending is {} for {}".format(result, user['acc_id']))
    return result

# def pancake_swap(driver, user, option):
#     password = option["password"]
#     driver.switch_to.window(driver.window_handles[0])
#     time.sleep(0.5)
#     network = "zkSync"
#     okx_connect_and_switch_network(driver, password, network)
#     driver.get("https://pancakeswap.finance/swap?chain=zkSync")
#     time.sleep(3)
#     if check_element_content(driver, "/html/body/div[1]/div[1]/div[1]/nav/div[2]/button/div[1]", "Connect", 5):
#         click(driver, "/html/body/div[1]/div[1]/div[1]/nav/div[2]/button")
#         click(driver, "/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/div[1]")
#         okxwallet_click(driver,
#             ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
#             "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm with gas change
#                     ],
#             30)
        
#     # try to sell eth
#     if not check_element_content(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/button/div/div", "ETH", 5):
#         click(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/button")
#         input_content(driver, "/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/input", "ETH")
#         time.sleep(2)
#         click(driver, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[1]")
#     coins = ['USDC', 'USDT']
#     random.shuffle(coins)
#     retry = 6
#     while retry > 0:
#         if check_element_content(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[2]", "Loading", 5):
#             time.sleep(5)
#             retry -= 1
#             logger.debug("wait for loading")
#         else:
#             break
#     amount = float(fetch_content(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[2]").split(":")[1])
#     logger.debug("{} eth".format(amount))
#     if amount > 0.01:
#         logger.debug("Has enough eth to sell")
#         gas_amount = round(random.uniform(0.001, 0.003), 6)
#         logger.debug("{} gas amount".format(gas_amount))
#         value_amount = round(amount - gas_amount, 5)
#         logger.debug("{} value amount".format(value_amount))
#         if not check_element_content(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/button/div/div", coins[0], 5):
#             click(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/button")
#             input_content(driver, "/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/input", coins[0])
#             time.sleep(2)
#             click(driver, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div")
#         input_content(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/div[2]/label/div[1]/input", value_amount)
#         time.sleep(1)
#         if check_element_content(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[5]/button", "Swap", 5):
#             click(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[5]/button")
#             click(driver, "/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button") # Confirm
#             okxwallet_click(driver,
#             ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
#             "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm with gas change
#                     ],
#             30)

#         time.sleep(10)
#         # _ = check_element_content(driver, "/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div", "receipt", 60)
#         click(driver, "/html/body/div[2]/div/div/div[2]/div/div[1]/button/svg") # Return to swap

#         time.sleep(3)
#         click(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[2]/div/button") # Switch
#         time.sleep(3)
#         click(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/div[2]/label/div[3]/div/button[4]") # MAX
#         time.sleep(3)
#         if check_element_content(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[5]/button", "Swap", 10):
#             click(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[5]/button")
#             click(driver, "/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button") # Confirm
#             okxwallet_click(driver,
#             ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
#             "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm with gas change
#                     ],
#             30)
#         try:
#             okxwallet_click(driver,
#             ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
#             "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm with gas change
#                     ],
#             30)
#         except:
#             pass
#         result = check_element_content(driver, "/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div", "receipt", 60)
#         logger.info("pancake swap is {} for {}".format(result, user['acc_id']))
#         return result
#     else:
#         click(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/button")
#         input_content(driver, "/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/input", coins[0])
#         time.sleep(2)
#         click(driver, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[1]")
#         time.sleep(3)
#         amount = float(fetch_content(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[2]").split(":")[1])
#         if amount < 0.01:
#             click(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/button")
#             input_content(driver, "/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/input", coins[1])
#             time.sleep(2)
#             click(driver, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[1]")
#         time.sleep(3)
#         amount = float(fetch_content(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[2]").split(":")[1])
#         if amount < 0.01:
#             logger.info("Not usdc or usdt to buy, pancake swap is False for {}".format(user['acc_id']))
#             return False
#         if not check_element_content(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/button/div/div", "ETH", 5):
#             click(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/button")
#             input_content(driver, "/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/input", "ETH")
#             time.sleep(2)
#             click(driver, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div")
#         click(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/div[2]/label/div[3]/div/button[4]") # MAX
#         time.sleep(3)
#         if check_element_content(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[5]/button", "Swap", 10):
#             click(driver, "/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[5]/button")
#             click(driver, "/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button") # Confirm
#             okxwallet_click(driver,
#             ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
#             "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm with gas change
#                     ],
#             30)
#         try:
#             okxwallet_click(driver,
#             ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
#             "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
#             "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm with gas change
#                     ],
#             30)
#         except:
#             pass
#         result = check_element_content(driver, "/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div", "receipt", 60)
#         logger.info("pancake swap is {} for {}".format(result, user['acc_id']))
#         return result