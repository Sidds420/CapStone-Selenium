class newaccountpg:
    def savings(self):
        acc_type = driver.find_element('xpath', '//select[@id="type"]')
        acc_select = Select(acc_type)
        acc_select.select_by_visible_text("SAVINGS")

    def new_account(self):
        driver.find_element('xpath', '//input[@value="Open New Account"]').click()

    def transfer_funds(self):
        driver.find_element('xpath', '//a[contains(text(),"Transfer Funds")]').click()