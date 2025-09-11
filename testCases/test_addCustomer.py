from pageObjects.AddCustomer import  AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadProperties
from testCases import conftest

class Test_003_addCustomer:
    pageUrl=ReadProperties.readPageURL()
    username=ReadProperties.readUsername()
    password=ReadProperties.readPassword()

    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.pageUrl)
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.driver.close()

    def test_addCus(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.pageUrl) 
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()

        ac=AddCustomer(self.driver)
        ac.click_menu_cus()
        ac.click_addNew()
        ac.addEmail("avii@gmail.com")
        ac.addPassword("Arav@123")
        ac.addFName("M")
        ac.addLName("Avii")
        ac.clickMale()
        ac.addCompany("QualiTlabs")
        ac.clickTax()
        ac.clickNewsLetter()
        ac.clickCusRoles()
        ac.selectVendor()
        ac.clickChangePassword()
        ac.clickSave()
