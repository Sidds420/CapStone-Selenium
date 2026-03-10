class homepg:
    def newaccount(self):
        driver.find_element('xpath', '//a[contains(text(),"Open New Account")]').click()

    def transfer_funds(self):
        driver.find_element('xpath', '//a[contains(text(),"Transfer Funds")]').click()

    def overview(self):
        driver.find_element('xpath', '//a[text()="Accounts Overview"]').click()

    def logout(self):
        driver.find_element('xpath', '//a[text()="Log Out"]').click()