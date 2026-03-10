from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

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
driver.find_element('xpath','//a[text()="Open New Account"]').click()
acc_type = driver.find_element('xpath','//select[@id="type"]')
acc_select = Select(acc_type)
acc_select.select_by_visible_text("SAVINGS")
driver.find_element('xpath','//input[@value="Open New Account"]').click()

#Transfer Funds
driver.find_element('xpath','//a[text()="Transfer Funds"]').click()
driver.find_element('xpath','//input[@id="amount"]').send_keys("100")

#From acc selection
# wait.until(
#     EC.presence_of_element_located(
#         ('xpath', '//select[@id="fromAccountId"]/option')
#     )
# )
# from_acc = driver.find_element('xpath','//select[@id="fromAccountId"]')
# from_select = Select(from_acc)
# from_select.select_by_value("43980")

#To account selection
# to_acc = driver.find_element('xpath','//select[@id="toAccountId"]')
# to_acc_select=Select(to_acc)
# to_acc_select.select_by_visible_text("43980")