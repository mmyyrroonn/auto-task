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
import time
from basic_operator import (
click,
fetch_content,input_content,
clear_windows_and_resize,switch_to_metamask,
check_element_content,input_password_and_unlock,
metamask_click)
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
    print('import complete')

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

def swith_to_twitter(driver):
    window_handles = driver.window_handles
    for handle in window_handles:
        # 切换到新窗口
        driver.switch_to.window(handle)
        
        # 如果确认是扩展窗口，则进行你需要的操作
        if "twitter" in driver.current_url:
            # 这里执行你想做的操作
            break

def import_twitter(driver, user):
    token = user['twitter'].split("----")[2].rstrip()
    handler = driver.current_window_handle
    driver.switch_to.window(handler)
    driver.get("https://twitter.com/")
    open_edit_cookie_and_swith(driver)
    driver.find_element('xpath', '/html/body/div[1]/nav/div/div/button').click() # click add cookie
    time.sleep(1)
    auth_input = driver.find_element('xpath', "/html/body/form[2]/div[2]/input")
    auth_input.clear()
    auth_input.send_keys("auth_token")
    time.sleep(0.5)
    auth_input = driver.find_element('xpath', "/html/body/form[2]/div[3]/textarea")
    auth_input.clear()
    auth_input.send_keys(token)
    time.sleep(0.5)
    driver.find_element('xpath', '/html/body/form[2]/div[5]/button').click() # click add cookie
    time.sleep(1)
    swith_to_twitter(driver)
    driver.refresh()
    time.sleep(5)

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
        print(driver.title)
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

def import_discord(driver, user):
    token = user['discord'].split("---")[-1].rstrip()
    handler = driver.current_window_handle
    driver.switch_to.window(handler)
    driver.get("https://discord.com/login")
    open_discord_login_and_swith(driver)
    time.sleep(0.5)
    auth_input = driver.find_element('xpath', "/html/body/div/div/div/input")
    auth_input.clear()
    auth_input.send_keys(token)
    time.sleep(0.5)
    driver.find_element('xpath', '/html/body/div/div/div/button').click() # click add cookie
    time.sleep(1)
    swith_to_discord(driver)

#### follow twitter users

def follow_user(driver, to_follow):
    driver.get("https://twitter.com/"+user)
    # Wait for the follow button to be clickable and then click it
    follow_button_xpath = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/span/span'
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, follow_button_xpath))).click()
    except:
        return
    time.sleep(1)

def follow_users(driver, _user, following):
    for to_follow in following:
        follow_user(driver, to_follow)

#### berachain daily drip
        
def bera_drip(driver, user):
    address = user["address"]
    handler = driver.current_window_handle
    driver.switch_to.window(handler)
    driver.get("https://artio.faucet.berachain.com/")
    time.sleep(0.5)
    input_content(driver, "/html/body/div[1]/div[2]/main/div/div[1]/div/div[2]/div[2]/div/input", address)
    time.sleep(0.5)
    click(driver, '/html/body/div[1]/div[2]/main/div/div[1]/div/button') # click
    time.sleep(0.5)
    click(driver, '/html/body/div[1]/div[2]/main/div/div[1]/div/button') # click
    time.sleep(0.5)
    # success
    content = fetch_content(driver, '/html/body/div[1]/div[2]/main/div/div[1]/div/div[3]/div')
    if "Please retry in 8 hours." in content:
        return False
    if "We are currently experiencing high traffic" in content:
        return False
    return True

#### import unisats memo
def import_unisat(driver, user, password):
    mnemonic = user["mnemonic"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("chrome-extension://ppbibelpcjmhbdihakflkdcoccbgbkpo/index.html")
    time.sleep(0.5)
    click(driver, "/html/body/div/div[1]/div/div/div/div[2]/div[3]") # already have
    time.sleep(0.5)
    input_content(driver, "/html/body/div/div[1]/div/div/div/div/div[3]/input", password)
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
    time.sleep(0.5)
    input_content(driver, "/html/body/div/div[1]/div/div/div/div/div[4]/input", password)
    time.sleep(0.5)
    click(driver, "/html/body/div/div[1]/div/div/div/div/div[5]") # already have
    time.sleep(0.5)
    click(driver, "/html/body/div/div[1]/div/div[2]/div[2]/div[2]") # UniSat Wallet
    for word in mnemonic:
        driver.switch_to.active_element.send_keys(word) # input each mnemonic to current textbox
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
    time.sleep(0.5)
    click(driver, "/html/body/div/div[1]/div/div[2]/div[2]/div[5]/div[2]/div") # continue
    time.sleep(0.5)
    click(driver, "/html/body/div/div[1]/div/div[2]/div[2]/div[10]/div[2]/div") # continue
    time.sleep(1)
    # time.sleep(3)
    # click(driver, "/html/body/div/div[1]/div/div[2]/div[2]/div/div/div[3]/div[2]/label/span[1]/input")
    # time.sleep(0.5)
    # click(driver, "/html/body/div/div[1]/div/div[2]/div[2]/div/div/div[3]/div[4]/label/span[1]/input")
    # time.sleep(0.5)
    # click(driver, "/html/body/div/div[1]/div/div[2]/div[2]/div/div/div[4]/div") # OK
    print("import unisat successufully")

#### well3 daily check
def well3_daily(driver, _user):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://well3.com/mission")
    time.sleep(0.5)
    click(driver, "/html/body/div/div[1]/main/section[1]/div[3]/div[2]/div[1]/div[1]/div/div/div[1]/div/div/div[5]/div[2]/button") # click start
    time.sleep(0.5)
    click(driver, "/html/body/div/div[1]/main/div[3]/div/div/button/div") # click i'm ready
    time.sleep(50)
    click(driver, "/html/body/div/div[1]/main/div[3]/div/div/button") # back to dashbord
    print("well3 daily success")

#### qna3 daily
def qna3_daily(driver, _user, password):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://qna3.ai/?code=jzfuvKpM")
    time.sleep(1)
    if check_element_content(driver, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div[4]/canvas", "", 3):
        click(driver, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div[4]")
        time.sleep(1)
        click(driver, "/html/body/div[6]/div/div/div/div/div[2]/button") # click sign out
        time.sleep(5)
        driver.get("https://qna3.ai/?code=jzfuvKpM")
        time.sleep(1)
        driver.get("https://qna3.ai/?code=jzfuvKpM")
        time.sleep(1)
        click(driver, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/button/span")
        time.sleep(1)
        click(driver, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/ul/li[1]/div") # click english
        time.sleep(2)
    if check_element_content(driver, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div[4]/button/span", "Sign", 5):
        click(driver, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div[4]/button") # click sign in
    time.sleep(1)
    click(driver, "/html/body/div[4]/div/div/div/div/div[2]/div/button") # click connect wallet
    time.sleep(0.5)
    click(driver, "/html/body/div[16]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/button/div/div/div[2]/div") # click metamask
    switch_to_metamask(driver)
    input_password_and_unlock(driver, password)
    metamask_click(driver, ["/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Approve
                                            "/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Switch
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Next
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Connect
                                            "/html/body/div[1]/div/div/div/div[4]/footer/button[2]"], # Sign
                                            30)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    click(driver, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/button/span")
    time.sleep(1)
    click(driver, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/ul/li[1]/div") # click english
    time.sleep(2)
    if check_element_content(driver, "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]", "opBNB", 10):
        print("click to opBNB")
        click(driver, "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]") # switch to opBNB
        metamask_click(driver, ["/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Approve
                                            "/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Switch
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Next
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Connect
                                            "/html/body/div[1]/div/div/div/div[4]/footer/button[2]"], # Sign
                                            30)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    click(driver, "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/div/button") # check-in
    switch_to_metamask(driver)
    time.sleep(0.5)
    click(driver, "/html/body/div[1]/div/div/div/div[3]/div[3]/footer/button[2]") # confirm
    driver.switch_to.window(driver.window_handles[0])
    result = check_element_content(driver, "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/div/a/button", "Claim Credits", 30)
    print("qan3 daily {}".format(result))

#### daily bera
def daily_bera_galxe_point(driver, user, password):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://galxe.com/Berachain/campaign/GCTN3ttM4T")
    time.sleep(0.5)
    switch_to_metamask(driver)
    input_password_and_unlock(driver, password)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    if check_element_content(driver, "/html/body/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[2]", "Log", 5):
        click(driver, "/html/body/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[1]/div[2]") # login in
        time.sleep(1)
        click(driver, "/html/body/div/div/div/div[3]/div[4]/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div") # metamask
        metamask_click(driver, ["/html/body/div[1]/div/div/div/div[5]/footer/button[2]"], 30)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
    click(driver, "/html/body/div/div/div/div[3]/div[1]/main/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/div/div[2]/div/div/div/button/div[1]/div[2]")
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(60)
    click(driver, "/html/body/div/div/div/div[3]/div[1]/main/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/div/div[2]/div/div/div/button/div[2]/div/div/div/div/div/div")
    time.sleep(5)
    click(driver, "/html/body/div/div/div/div[3]/div[1]/main/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/button")
    time.sleep(5)
    print("bera point daily get")

#### well3 daily check
def well3_daily_mint(driver, _user, password):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://well3.com/mission")
    time.sleep(0.5)
    click(driver, "/html/body/div/div[1]/header/div/div[1]/a/div/img") # click start
    time.sleep(1)
    click(driver, "/html/body/div/div[2]/div/div[2]/div/div/div[1]/div/nav/ol/li[5]/a/span") # click master's wisdom
    time.sleep(1)
    click(driver, "/html/body/div/div[1]/main/div/div[2]/div[1]/div[5]/button") # connect wallet
    time.sleep(0.5)
    click(driver, "/html/body/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/button/div/div/div[2]") # click metamask
    switch_to_metamask(driver)
    input_password_and_unlock(driver, password)
    time.sleep(2)
    metamask_click(driver, ["/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Approve
                                            "/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Switch
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Next
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Connect
                                            "/html/body/div[1]/div/div/div/div[4]/footer/button[2]"], # Sign
                                            30)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    if check_element_content(driver, "/html/body/div/div[1]/main/div/div[2]/div[1]/div[5]/button", "Link", 3):
        click(driver, "/html/body/div/div[1]/main/div/div[2]/div[1]/div[5]/button") # Link
        time.sleep(1)
        metamask_click(driver, ["/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Approve
                                            "/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Switch
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Next
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Connect
                                            "/html/body/div[1]/div/div/div/div[4]/footer/button[2]"], # Sign
                                            30)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    if check_element_content(driver, "/html/body/div/div[1]/main/div/div[2]/div[1]/div[5]/button", "Switch", 3):
        click(driver, "/html/body/div/div[1]/main/div/div[2]/div[1]/div[5]/button") # Switch
        time.sleep(1)
        metamask_click(driver, ["/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Approve
                                            "/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Switch
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Next
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Connect
                                            "/html/body/div[1]/div/div/div/div[4]/footer/button[2]"], # Sign
                                            30)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    if check_element_content(driver, "/html/body/div/div[1]/main/div/div[2]/div[1]/div[5]/div[2]", "", 3):
        click(driver, "/html/body/div/div[1]/main/div/div[2]/div[1]/div[5]/div[2]")
    else:
        click(driver, "/html/body/div/div[1]/main/div/div[2]/div[1]/div[5]/div[2]/div[2]") # free
    time.sleep(1)
    click(driver, "/html/body/div/div[1]/div[4]/div/div/div/div/div") # mint
    switch_to_metamask(driver)
    metamask_click(driver, ["/html/body/div[1]/div/div/div/div[3]/div[3]/footer/button[2]", # Check
                                            "/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Switch
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Next
                                            "/html/body/div[1]/div/div/div/div[4]/footer/button[2]"], # Sign
                                            30)
    time.sleep(2)
    print("well3 daily mint success")

def nfp_daily_check(driver, _user, password):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://nfprompt.io/earn?invitecode=1bX2Jmzj")
    time.sleep(1)
    click(driver, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/button/span")
    time.sleep(1)
    click(driver, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div/div[1]/span")
    time.sleep(2)
    ### tricky solution for wallet connect
    driver.execute_script(
    """document.querySelector('w3m-modal').shadowRoot.querySelector('w3m-modal-router').shadowRoot.querySelector('w3m-connect-wallet-view').shadowRoot.querySelector('w3m-desktop-wallet-selection').shadowRoot.querySelector('w3m-modal-footer').querySelector('div.w3m-grid').querySelector('w3m-wallet-button').shadowRoot.querySelector('button').click();""")
    time.sleep(1)
    switch_to_metamask(driver)
    input_password_and_unlock(driver, password)
    time.sleep(2)
    metamask_click(driver, ["/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Approve
                                            "/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Switch
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Next
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Connect
                                            "/html/body/div[1]/div/div/div/div[4]/footer/button[2]"], # Sign
                                            30)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    click(driver, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/button/span")
    switch_to_metamask(driver)
    time.sleep(0.5)
    click(driver, "/html/body/div[1]/div/div/div/div[3]/div[3]/footer/button[2]") # confirm
    driver.switch_to.window(driver.window_handles[0])
    result = check_element_content(driver, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/span", ":", 30)
    print("nfp daily {}".format(result))


# chrome-extension://nebnhfamliijlghikdgcigoebonmoibm/fullpage.html#/ aleo wallet
