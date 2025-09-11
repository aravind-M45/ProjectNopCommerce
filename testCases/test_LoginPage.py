import pytest
from selenium import webdriver
from utilities.readProperties import ReadProperties
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen

class Test_001_LoginPage:

    page_url=ReadProperties.readPageURL()
    username=ReadProperties.readUsername()
    password=ReadProperties.readPassword()
    logger=LogGen.logGen()

    def test_homePage(self,setup):
        self.logger.info("*************************Test Login Page**********************")
        self.logger.info("*************************Started******************************")
        self.driver=setup
        self.driver.get(self.page_url)
        act_title=self.driver.title
        if act_title=="nopCommerce demo store. Login":
            self.logger.info("***********************HomePage Title is Verified***************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\homePageDetails.png")
            self.logger.error("***********************HomePage Title is Not Verified***************")
            assert False
            self.driver.close()

    def test_loginDetails(self,setup):
        self.driver=setup
        self.driver.get(self.page_url)
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        actual_title=self.driver.title
        print(actual_title,"------------------------------------->")
        lp.clickLogout()
        if actual_title=="Dashboard / nopCommerce administration":
            self.logger.info("***********************Login Credentials are Verified***************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\loginDetails.png")
            self.logger.error("***********************Login Credentials are Not Verified***************")
            self.driver.close()
            assert False


