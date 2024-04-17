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
metamask_click, switch_to_network, wait_for_continue)

def init_connect_and_scan(driver, user, option):
    password = option["password"]
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get("https://secwarex.io?channelCode=CV15AE50")
    click(driver, "/html/body/div/div[1]/div[2]/div[1]/div/div[1]/div[3]/div[4]") # Connect
    wait_for_continue(user)
    click(driver, "/html/body/div[1]/div[3]/div/div/div[2]/div[1]")
    switch_to_metamask(driver)
    input_password_and_unlock(driver, password)
    metamask_click(driver, ["/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Approve
                                            "/html/body/div[1]/div/div/div/div[2]/div/button[2]", # Switch
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Next
                                            "/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]", # Connect
                                            "/html/body/div[1]/div/div/div/div[4]/footer/button[2]"], # Sign
                                            30)
    time.sleep(1)
    click(driver, "/html/body/div[1]/div[1]/div[1]/div/img[2]")
    click(driver, "/html/body/div/div[1]/div[2]/div/img[2]")
    click(driver, "/html/body/div/div[1]/div[3]/div/img[2]")
    click(driver, "/html/body/div/div[1]/div[4]/div/img[2]")
    time.sleep(1)
    click(driver, "/html/body/div/div[1]/div[2]/div[1]/div/div[1]/div[3]/div[2]/div[1]")
    results = check_element_content(driver, "/html/body/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[4]/span", "Security", 60)
    logger.info("init secwarex is {}".format(results))
    return results
