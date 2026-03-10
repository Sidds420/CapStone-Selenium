class RegisterPg:

    def __init__(self, driver):
        self.driver = driver

    def first_name(self):
        self.driver.find_element('xpath','//input[@name="customer.firstName"]').send_keys("SK")

    def last_name(self):
        self.driver.find_element('xpath','//input[@name="customer.lastName"]').send_keys("Mohla")

    def address(self):
        self.driver.find_element('xpath','//input[@name="customer.address.street"]').send_keys("Whitefield")

    def city(self):
        self.driver.find_element('xpath','//input[@name="customer.address.city"]').send_keys("Bengaluru")

    def state(self):
        self.driver.find_element('xpath','//input[@name="customer.address.state"]').send_keys("Karnataka")

    def zip(self):
        self.driver.find_element('xpath','//input[@name="customer.address.zipCode"]').send_keys("500106")

    def phone(self):
        self.driver.find_element('xpath','//input[@name="customer.phoneNumber"]').send_keys("9456789054")

    def ssn(self):
        self.driver.find_element('xpath','//input[@name="customer.ssn"]').send_keys("123456789")

    def username(self):
        self.driver.find_element('xpath','//input[@id="customer.username"]').send_keys("SKMohla")

    def password(self):
        self.driver.find_element('xpath','//input[@id="customer.password"]').send_keys("ApneKaamSeKaam123")

    def confirmpassword(self):
         self.driver.find_element('xpath','//input[@id="repeatedPassword"]').send_keys("ApneKaamSeKaam123")

    def click_register(self):
        self.driver.find_element('xpath','//input[@value="Register"]').click()