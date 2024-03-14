from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import (NoSuchElementException,
                                        TimeoutException,
                                        ElementClickInterceptedException,
                                        WebDriverException)
import time

def click(driver, xpath):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    time.sleep(0.5)
    
def fetch_content(driver, xpath):
    text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath))).text
    time.sleep(0.5)
    return text

def input_content(driver, xpath, content):
    input_content = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    input_content.clear()
    input_content.send_keys(content)
    time.sleep(0.5)

def clear_windows_and_resize(driver):
    all_windows = driver.window_handles

    # 保留第一个窗口，关闭其他窗口
    for window in all_windows[1:]:
        driver.switch_to.window(window)
        driver.close()
    driver.switch_to.window(all_windows[0])

    # 修改窗口大小，例如设置宽度为1024px，高度为768px
    driver.set_window_size(1980, 1280)
    time.sleep(0.5)

def switch_to_metamask(driver, max_wait_time=15):
    end_time = time.time() + max_wait_time
    metamask_found = False

    while True:
        all_windows = driver.window_handles
        for window in all_windows:
            driver.switch_to.window(window)
            if "MetaMask" in driver.title:
                metamask_found = True
                break
        
        if metamask_found or time.time() > end_time:
            break
        
        time.sleep(0.5)  # Wait for 0.5 seconds before trying again
    
    if not metamask_found:
        raise TimeoutException("MetaMask window did not appear within the maximum wait time.")

def check_element_content(driver, xpath: str, content: str, max_wait_time: int) -> bool:
    end_time = time.time() + max_wait_time
    while True:
        try:
            # Find the element using the provided XPath
            element = driver.find_element('xpath', xpath)
            # If the element's text matches the expected content, return True
            if content in element.text:
                return True
        except NoSuchElementException:
            # If the element is not found, we'll wait and retry
            pass
        
        # Check if the timeout has been reached
        if time.time() > end_time:
            break
        
        # Wait for 1 second before trying again
        time.sleep(1)
    
    # If the element was not found or content did not match within the max_wait_time, return False
    return False

def metamask_notification_check(driver):
    all_windows = driver.window_handles
    metamask_found = False
    print("all_windows", all_windows)
    for window in all_windows:
        try:
            driver.switch_to.window(window)
            if "Notification" in driver.title:
                if check_element_content(driver, "/html/body/div[2]/div/div/section/div[3]/button", "", 2):
                    click(driver, "/html/body/div[2]/div/div/section/div[3]/button") # got it
        except WebDriverException as e:
                # Check if the exception is because of a closed driver
                if 'no such window' in str(e).lower():
                    continue
                else:
                    return False
    all_windows = driver.window_handles 
    for window in all_windows:
        driver.switch_to.window(window)
        if "MetaMask" in driver.title:
            metamask_found = True
            break
    return metamask_found

def metamask_click(driver, xpaths: [str], max_wait_time: int) -> bool:
    time.sleep(2) # wait for the tab
    end_time = time.time() + max_wait_time
    consecutive_closures = 0  # Counter for consecutive driver closures

    while True:
        print("check1")
        time.sleep(1)
        metamask_found = metamask_notification_check(driver)
        if time.time() > end_time:
            break
        time.sleep(1)
        if not metamask_found:
            print("not found")
            consecutive_closures += 1
            if consecutive_closures >= 3:
                return True
            continue
        print("check3")
        for xpath in xpaths:
            try:
                # Check if the element exists and is visible
                element = driver.find_element('xpath', xpath)
                print("check4")
                consecutive_closures = 0
                if element.is_displayed():
                    # Click on the element if it is displayed
                    element.click()
                    break
            except (NoSuchElementException, ElementClickInterceptedException):
                print("check5")
                continue  # If exception occurs, move to the next xpath
            except WebDriverException as e:
                # Check if the exception is because of a closed driver
                if 'no such window' in str(e).lower():
                    consecutive_closures += 1
                    if consecutive_closures >= 5:
                        print("Driver has been closed consecutively 5 times. Ending function.")
                        return True
                else:
                    # If the error is not due to a closed driver, reset the counter
                    consecutive_closures = 0
    return True

def input_password_and_unlock(driver, password):
    input_content(driver, "/html/body/div[1]/div/div/div/div/form/div/div/input", password)
    time.sleep(0.5)
    click(driver, "/html/body/div[1]/div/div/div/div/button") # unlock

def fetch_value(driver, xpath, max_wait_time=5):
    end_time = time.time() + max_wait_time
    while True:
        try:
            # Find the element using the provided XPath
            element = driver.find_element('xpath', xpath)
            # If the element's text matches the expected content, return True
            return element.text
        except NoSuchElementException:
            # If the element is not found, we'll wait and retry
            pass
        
        # Check if the timeout has been reached
        if time.time() > end_time:
            break
        
        # Wait for 1 second before trying again
        time.sleep(1)
    time.sleep(0.5)
