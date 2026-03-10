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
driver.find_element('xpath','//input[@name="customer.address.street"]').send_keys("Whitefield")
driver.find_element('xpath','//input[@name="customer.address.city"]').send_keys("Bengaluru")
driver.find_element('xpath','//input[@name="customer.address.state"]').send_keys("Karnataka")
driver.find_element('xpath','//input[@name="customer.address.zipCode"]').send_keys("500106")
driver.find_element('xpath','//input[@name="customer.phoneNumber"]').send_keys("9456789054")
driver.find_element('xpath','//input[@name="customer.ssn"]').send_keys("123456789")
driver.find_element('xpath','//input[@value="Register"]').click()


# Login
driver.find_element['xpath','//input[@name="username"]'].send_keys("SK")
driver.find_element['xpath','//input[@name="password"]'].send_keys("")
driver.find_element['xpath','//input[@value="Log In"]'].click()
time.sleep(2)