from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver=webdriver.Chrome(opts)
wait = WebDriverWait(driver,10)

driver.get("https://parabank.parasoft.com/")
driver.maximize_window()
time.sleep(2)

#Register
driver.find_element('xpath','//a[text()="Register"]').click()
driver.find_element('xpath','//input[@name="customer.firstName"]').send_keys("SK")
driver.find_element('xpath','//input[@name="customer.lastName"]').send_keys("Mohla")


