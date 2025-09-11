import time

import pytest
from selenium import webdriver
from utilities.readProperties import ReadProperties
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities import XlUtils
class Test_002_LoginPageDD:

    page_url=ReadProperties.readPageURL()
    file=r".\\testData\\LoginData.xlsx"
    logger=LogGen.logGen()
    def test_loginDetails_dd(self,setup):
        self.driver=setup
        self.driver.get(self.page_url)
        lp=LoginPage(self.driver)
        rows=XlUtils.getRowCount(self.file,"Sheet1")
        self.logger.info("*********************Test_002_LoginPageDD************************")

        lst=[]
        for r in range(2,rows+1):
            username=XlUtils.readData(self.file,"Sheet1",r,1)
            password=XlUtils.readData(self.file,"Sheet1",r,2)
            exp_res=XlUtils.readData(self.file,"Sheet1",r,3)
            lp.setUserName(username)
            lp.setPassword(password)
            lp.clickLogin()
            time.sleep(2)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if exp_res=="Pass":
                    self.logger.info("**Pass**")
                    lp.clickLogout()
                    lst.append("Pass")
                elif exp_res=="Fail":
                    self.logger.info("**Fail**")
                    lp.clickLogout()
                    lst.append("Fail")

            elif act_title!=exp_title:
                if exp_res=="Pass":
                    self.logger.info("**Fail**")
                    lst.append("Fail")
                elif exp_res=="Fail":
                    self.logger.info("**Pass**")
                    lst.append("Pass")



        if "Fail" not in lst:
            self.logger.info("**Test_DD Passed**")
            self.driver.close()
        else:
            self.logger.info("**Test_DD Failed**")
            self.driver.close()