class Transferpg:
    def amount(self):
        driver.find_element('xpath', '//input[@id="amount"]').send_keys("5")

    def to_account(selfself):
        driver.find_element('xpath', '//select[@id="toAccountId"]').click()
        wait.until(ec.presence_of_element_located(('xpath', '//select[@id="toAccountId"]/option[2]')))
        driver.find_element('xpath', '//select[@id="toAccountId"]/option[2]').click()
        driver.find_element('xpath', '//input[@type="submit"]').click()

        try:
            wait.until(ec.visibility_of_element_located(('xpath', '//h1[contains(text(),"Transfer Complete!")]')))
            print("Fund transfer complete!")
        except:
            print("Fund transfer failed")

    def overview(self):
        driver.find_element('xpath', '//a[text()="Accounts Overview"]').click()