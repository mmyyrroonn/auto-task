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
from loguru import logger

def wait_for_continue(user):
    while True:
        # 等待用户输入
        user_input = input("Please enter the acc id to continue: ")
        
        # 尝试将输入转换为整数
        try:
            input_number = int(user_input)

            # 判断输入的数字是否在user中
            if input_number == user["acc_id"]:
                print("{} back to auto work".format(input_number))
                time.sleep(1)
                return True
        except ValueError:
            # 如果输入不能转换成整数，则返回False
            print("That's not a valid number.")

def switch_to_page(driver, url, max_wait_time=120):
    end_time = time.time() + max_wait_time
    page_found = False
    while True:
        all_windows = driver.window_handles
        for window in all_windows:
            driver.switch_to.window(window)
            if url in driver.current_url:
                page_found = True
                break
        
        if page_found or time.time() > end_time:
            break
        
        time.sleep(1)  # Wait for 0.5 seconds before trying again


def switch_to_network(driver, user, option):
    network_id = option["network_id"]
    password = option["password"]
    network_url = "https://chainlist.org/chain/" + network_id
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.get(network_url)
    click(driver, "/html/body/div[1]/div/div[2]/div[2]/button")
    switch_to_okwallet(driver)
    input_password_and_unlock_okxwallet(driver, password)
    okx_wallet_confirm(driver)
    driver.switch_to.window(driver.window_handles[0])

def click(driver, xpath):
    logger.debug("click {}".format(xpath))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    time.sleep(0.5)
    
def fetch_content(driver, xpath):
    text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath))).text
    logger.debug("fetch_content text is  {}".format(text))
    time.sleep(0.5)
    return text

def input_content(driver, xpath, content):
    input_content = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    input_content.clear()
    for _ in range(len(input_content.get_attribute('value'))):
        input_content.send_keys(Keys.BACKSPACE)
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
            logger.debug("check_element_content text is {}".format(element.text))
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
    logger.debug("all_windows", all_windows)
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
        logger.debug("check1")
        time.sleep(1)
        metamask_found = metamask_notification_check(driver)
        if time.time() > end_time:
            break
        time.sleep(1)
        if not metamask_found:
            logger.debug("not found")
            consecutive_closures += 1
            if consecutive_closures >= 3:
                return True
            continue
        logger.debug("check3")
        for xpath in xpaths:
            try:
                # Check if the element exists and is visible
                element = driver.find_element('xpath', xpath)
                logger.debug("check4")
                consecutive_closures = 0
                if(element and element.is_displayed()):
                    # Click on the element if it is displayed
                    element.click()
                    break
            except (NoSuchElementException, ElementClickInterceptedException):
                logger.debug("check5")
                continue  # If exception occurs, move to the next xpath
            except WebDriverException as e:
                # Check if the exception is because of a closed driver
                if 'no such window' in str(e).lower():
                    consecutive_closures += 1
                    if consecutive_closures >= 10:
                        logger.debug("Driver has been closed consecutively 5 times. Ending function.")
                        return True
                else:
                    # If the error is not due to a closed driver, reset the counter
                    consecutive_closures = 0
    return True

def input_password_and_unlock(driver, password):
    input_content(driver, "/html/body/div[1]/div/div/div/div/form/div/div/input", password)
    time.sleep(0.5)
    click(driver, "/html/body/div[1]/div/div/div/div/button") # unlock

def fetch_attribute(driver, xpath, attribute, max_wait_time=5):
    end_time = time.time() + max_wait_time
    while True:
        try:
            # Find the element using the provided XPath
            element = driver.find_element('xpath', xpath)
            # If the element's text matches the expected content, return True
            return element.get_attribute(attribute)
        except NoSuchElementException:
            # If the element is not found, we'll wait and retry
            pass
        
        # Check if the timeout has been reached
        if time.time() > end_time:
            break
        
        # Wait for 1 second before trying again
        time.sleep(1)
    time.sleep(0.5)

def check_content_color(driver, xpath, color, max_wait_time: int):
    end_time = time.time() + max_wait_time
    while True:
        try:
            # Find the element using the provided XPath
            element = driver.find_element('xpath', xpath)
            # If the element's text matches the expected content, return True
            if color == element.value_of_css_property('color'):
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

def switch_to_okwallet(driver, max_wait_time=15):
    end_time = time.time() + max_wait_time
    okwallet_found = False

    while True:
        okwallet_found = found_okxwallet(driver)
        
        if okwallet_found or time.time() > end_time:
            break
        
        time.sleep(0.5)  # Wait for 0.5 seconds before trying again
    
    if not okwallet_found:
        raise TimeoutException("MetaMask window did not appear within the maximum wait time.")
    
def found_okxwallet(driver):
    all_windows = driver.window_handles
    logger.debug(all_windows)
    if not all_windows:
        return False
    for window in all_windows:
        try:
            driver.switch_to.window(window)
            if "OKX Wallet" in driver.title:
                return True
        except:
            return False
    return False

def input_password_and_unlock_okxwallet(driver, password):
    input_content(driver, "/html/body/div[1]/div/div/div/div[3]/form/div[1]/div/div/div/div/div/input", password)
    time.sleep(0.5)
    click(driver, "/html/body/div[1]/div/div/div/div[3]/form/div[2]/div/div/div/button") # unlock

def okxwallet_click(driver, xpaths: [str], max_wait_time: int) -> bool:
    time.sleep(2) # wait for the tab
    end_time = time.time() + max_wait_time
    consecutive_closures = 0  # Counter for consecutive driver closures

    while True:
        logger.debug("check1")
        time.sleep(1)
        okxwallet_found = found_okxwallet(driver)
        if time.time() > end_time:
            break
        time.sleep(1)
        if not okxwallet_found:
            logger.debug("not found")
            consecutive_closures += 1
            if consecutive_closures >= 3:
                return True
            continue
        logger.debug("check3")
        for xpath in xpaths:
            try:
                # Check if the element exists and is visible
                element = driver.find_element('xpath', xpath)
                logger.debug("check4")
                consecutive_closures = 0
                if(element and element.is_displayed()):
                    # Click on the element if it is displayed
                    element.click()
                    break
            except (NoSuchElementException, ElementClickInterceptedException):
                logger.debug("check5")
                continue  # If exception occurs, move to the next xpath
            except WebDriverException as e:
                # Check if the exception is because of a closed driver
                if 'no such window' in str(e).lower():
                    consecutive_closures += 1
                    if consecutive_closures >= 10:
                        logger.debug("Driver has been closed consecutively 5 times. Ending function.")
                        return True
                else:
                    # If the error is not due to a closed driver, reset the counter
                    consecutive_closures = 0
    return True

def okx_connect_and_switch_network(driver, password, network):
    driver.get("chrome-extension://mcohilncbfahbmgdjkbpemcciiolgcge/home.html#home")
    input_password_and_unlock_okxwallet(driver, password)
    if network is not None:
        driver.get("chrome-extension://mcohilncbfahbmgdjkbpemcciiolgcge/home.html#connect-site")
        if not check_element_content(driver, "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[2]/div/span", network, 5):
            click(driver, "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[2]/div/span")
            input_content(driver, "/html/body/div[1]/div/div/div[3]/div/div[3]/div/div/div[2]/div[1]/div/input[2]", network)
            time.sleep(3)
            click(driver, "/html/body/div[1]/div/div/div[3]/div/div[3]/div/div/div[2]/div[2]/div[2]/span")

def click_white_space(driver, x_coordinate = 10, y_coordinate = 10):
    script = f"document.elementFromPoint({x_coordinate}, {y_coordinate}).click();"
    driver.execute_script(script)
    time.sleep(1)

def okx_wallet_confirm(driver):
    okxwallet_click(driver,
        ["/html/body/div[1]/div/div/div/div/div[5]/div[2]/button[2]", # Connect
        "/html/body/div[1]/div/div/div/div[2]/div/div[7]/div[2]/button[2]", # Fill up GLMR
        "/html/body/div[1]/div/div/div/div/div/div[7]/div[2]/button[2]", # Confirm
        "/html/body/div[1]/div/div/div/div/div/div[5]/div/button[2]", # Confirm
        "/html/body/div[1]/div/div/div/div/div/div[7]/div/button[2]", # Confirm
        "/html/body/div[1]/div/div/div/div[5]/div/button[2]", # Confirm
        "/html/body/div[1]/div/div/div/div[8]/div/button[2]", # Confirm
        ],
        30)