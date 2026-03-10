from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver=webdriver.Chrome()
wait = WebDriverWait(driver,10)

driver.get("https://parabank.parasoft.com/")
driver.maximize_window()
time.sleep(2)

# Login
driver.find_element['xpath','//input[@name="username"]'].send_keys("SK")
driver.find_element['xpath','//input[@name="password"]'].send_keys("")
driver.find_element['xpath','//input[@value="Log In"]'].click()
time.sleep(2)