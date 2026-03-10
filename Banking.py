import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver=webdriver.Chrome(opts)
wait = WebDriverWait(driver,10)

driver.get("https://parabank.parasoft.com/")
driver.maximize_window()
time.sleep(2)

#Register
# driver.find_element('xpath','//a[text()="Register"]').click()
# driver.find_element('xpath','//input[@name="customer.firstName"]').send_keys("SK")
# driver.find_element('xpath','//input[@name="customer.lastName"]').send_keys("Mohla")
# driver.find_element('xpath','//input[@name="customer.address.street"]').send_keys("Whitefield")
# driver.find_element('xpath','//input[@name="customer.address.city"]').send_keys("Bengaluru")
# driver.find_element('xpath','//input[@name="customer.address.state"]').send_keys("Karnataka")
# driver.find_element('xpath','//input[@name="customer.address.zipCode"]').send_keys("500106")
# driver.find_element('xpath','//input[@name="customer.phoneNumber"]').send_keys("9456789054")
# driver.find_element('xpath','//input[@name="customer.ssn"]').send_keys("123456789")
# driver.find_element('xpath','//input[@id="customer.username"]').send_keys("SKMohla")
# driver.find_element('xpath','//input[@id="customer.password"]').send_keys("ApneKaamSeKaam123")
# driver.find_element('xpath','//input[@id="repeatedPassword"]').send_keys("ApneKaamSeKaam123")
# driver.find_element('xpath','//input[@value="Register"]').click()
# time.sleep(2)

# Login
driver.find_element('xpath','//input[@name="username"]').send_keys("SKMohla")
driver.find_element('xpath','//input[@name="password"]').send_keys("ApneKaamSeKaam123")
driver.find_element('xpath','//input[@value="Log In"]').click()
time.sleep(2)

#OpenNewAccount
driver.find_element('xpath','//a[contains(text(),"Open New Account")]').click()
acc_type = driver.find_element('xpath','//select[@id="type"]')
acc_select = Select(acc_type)
acc_select.select_by_visible_text("SAVINGS")
driver.find_element('xpath','//input[@value="Open New Account"]').click()

#Transfer Funds
driver.find_element('xpath','//a[contains(text(),"Transfer Funds")]').click()
driver.find_element('xpath','//input[@id="amount"]').send_keys("5")
driver.find_element('xpath','//select[@id="toAccountId"]').click()
wait.until(ec.presence_of_element_located(('xpath','//select[@id="toAccountId"]/option[2]')))
driver.find_element('xpath','//select[@id="toAccountId"]/option[2]').click()
driver.find_element('xpath','//input[@type="submit"]').click()

try:
    wait.until(ec.visibility_of_element_located(('xpath', '//h1[contains(text(),"Transfer Complete!")]')))
    print("Fund transfer complete!")
except:
    print("Fund transfer failed")

#Account Overview
driver.find_element('xpath','//a[text()="Accounts Overview"]').click()

#Account LogOut
driver.find_element('xpath','//a[text()="Log Out"]').click()