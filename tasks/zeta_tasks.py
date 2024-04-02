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

def mint_and_stake_zeta_in_accumulated(driver, user, option):
    option["network_id"] = "7000"
    switch_to_network(driver, user, option)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://accumulated.finance/stake/zeta")
    if check_element_content(driver, "/html/body/div[1]/div/div/header/div/div[3]/div[2]/button", "Connect Wallet", 10):
        click(driver, "/html/body/div[1]/div/div/header/div/div[3]/div[2]/button")
        click(driver, "/html/body/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/button/div/div")
        switch_to_metamask(driver)
        metamask_click(driver, ["/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Approve
                                            "/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Switch
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Next
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Connect
                                            "/html/body/div[1]/div/div/div/div[4]/footer/button[2]"], # Sign
                                            30)
        driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    stake_amount = random.uniform(0.0001, 0.0002)
    input_content(driver, "/html/body/div[1]/div/div/div[3]/div[2]/div[1]/div/div[2]/div[1]/div[1]/input", stake_amount)
    time.sleep(1)
    click(driver, "/html/body/div[1]/div/div/div[3]/div[2]/div[1]/div/div[2]/div[3]/div[3]/button")
    switch_to_metamask(driver)
    metamask_click(driver, ["/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Approve
                                        "/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Switch
                                        "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Next
                                        "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Connect
                                        "/html/body/div[1]/div/div/div/div[4]/footer/button[2]"], # Sign
                                        30)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(20)
    click(driver, "/html/body/div[1]/div/div/div[3]/div[2]/div[1]/div/div[1]/button[2]")
    click(driver, "/html/body/div[1]/div/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/a")
    try:
        click(driver, "/html/body/div[1]/div/div/div[3]/div[2]/div[1]/div/div[3]/div[3]/div[3]/button[1]")
        switch_to_metamask(driver)
        metamask_click(driver, ["/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Approve
                                            "/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Switch
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Next
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Connect
                                            "/html/body/div[1]/div/div/div/div[4]/footer/button[2]"], # Sign
                                            30)
    except:
        pass
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(10)
    click(driver, "/html/body/div[1]/div/div/div[3]/div[2]/div[1]/div/div[3]/div[3]/div[3]/button[2]")
    switch_to_metamask(driver)
    metamask_click(driver, ["/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Approve
                                        "/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Switch
                                        "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Next
                                        "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Connect
                                        "/html/body/div[1]/div/div/div/div[4]/footer/button[2]"], # Sign
                                        30)
    
def zetahub_register(driver, user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://hub.zetachain.com/zh-CN/xp?code=YWRkcmVzcz0weDc4MUVFNTllYzRiNjIzZUE1YjgxNEQ4YzljM0RiMDM5MDFBYzY1MjMmZXhwaXJhdGlvbj0xNzEyMzk4MzU1JnI9MHg3OGIxNzYyZDJkNGU0N2UyYzEwOGUxM2NjMjc0NWRjYzVlMDBhOWFjMjhkYmI5YTQzOTY2ZDJmYWE4NmE2NWNjJnM9MHg2Mjc4YWJlODdhOWE2N2NmOTNjMjcwODE1MTMyYjg4ODM1")
    check_element_content(driver, "/html/body/div[1]/div/div/main/div[2]/div/div[1]/div/div[2]/div[2]/div/button", "", 60)
    click(driver, "/html/body/div[1]/div/div/main/div[2]/div/div[1]/div/div[2]/div[2]/div/button")
    click(driver, "/html/body/div[5]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[1]/button/div/div")
    switch_to_metamask(driver)
    input_password_and_unlock(driver, password)
    metamask_click(driver, ["/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Approve
                                        "/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Switch
                                        "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Next
                                        "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Connect
                                        "/html/body/div[1]/div/div/div/div[4]/footer/button[2]"], # Sign
                                        30)
    driver.switch_to.window(driver.window_handles[0])
    click(driver, "/html/body/div[1]/div/div/main/div[2]/div/div[1]/div/div[2]/div[2]/div/button")
    result = check_element_content(driver, "/html/body/div[1]/div/div/main/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[3]/p[1]", "2024", 30)
    logger.info("zetahub register is {} for {}".format(result, user["acc_id"]))
    return result
    