import time

class loginpg:
    def enter_email(self):
        driver.find_element('xpath','//input[@name="username"]').send_keys("SKMohla")

    def enter_password(self):
        driver.find_element('xpath', '//input[@name="password"]').send_keys("ApneKaamSeKaam123")

    def login(self):
        driver.find_element('xpath', '//input[@value="Log In"]').click()
        time.sleep(2)

    def register(self):
        driver.find_element('xpath', '//a[text()="Register"]').click()