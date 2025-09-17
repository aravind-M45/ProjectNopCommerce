from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testCases.test_LoginPage import Test_001_LoginPage


class AddCustomer:
    btn_menucus_xpath="/html/body/div[3]/aside/div/nav/ul/li[4]/a/p"
    btn_subcus_xpath="//p[text()=' Customers']"
    btn_addnew_xpath="//a[@class='btn btn-primary']"
    txtbox_email_xpath="//input[@id='Email']"
    txtbox_password_xpath="//input[@id='Password']"
    txtbox_fname_ID="FirstName"
    txtbox_lname_ID="LastName"
    rbtn_male_ID="Gender_Male"
    txtbox_compname_ID="Company"
    txtbox_tax_ID="IsTaxExempt"
    drpdwn_newLetter_xpath="//*[@id='customer-info']/div[2]/div[8]/div[2]/div/div[1]/div/span/span[1]/span"
    drpdwn_newLetterNop_xpath="//li[text()='nopCommerce admin demo store']"
    btn_cusroleRemove_xpath="//span[@role='presentation']"
    btn_cusroleAdd_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-rs09-1']"
    select_manOfVend_xpath="//select[@id='VendorId']"
    rbtn_changepass_xpath="//input[@id='MustChangePassword']"
    btn_save_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def click_menu_cus(self):
        self.driver.find_element(By.XPATH,self.btn_menucus_xpath).click()
        self.driver.find_element(By.XPATH,self.btn_subcus_xpath).click()

    def click_addNew(self):
        self.driver.find_element(By.XPATH,self.btn_addnew_xpath).click()

    def addEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtbox_email_xpath).send_keys(email)

    def addPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtbox_password_xpath).send_keys(password)

    def addFName(self,fname):
        self.driver.find_element(By.ID,self.txtbox_fname_ID).send_keys(fname)

    def addLName(self,lname):
        self.driver.find_element(By.ID,self.txtbox_lname_ID).send_keys(lname)

    def clickMale(self):
        self.driver.find_element(By.ID,self.rbtn_male_ID).click()

    def addCompany(self,company):
        self.driver.find_element(By.ID,self.txtbox_compname_ID).send_keys(company)

    def clickTax(self):
        self.driver.find_element(By.ID,self.txtbox_tax_ID).click()

    def clickNewsLetter(self):
        self.driver.find_element(By.XPATH,self.drpdwn_newLetter_xpath).click()
        self.driver.find_element(By.XPATH,self.drpdwn_newLetterNop_xpath).click()

    def clickCusRoles(self):
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH,self.btn_cusroleRemove_xpath))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,self.btn_cusroleAdd_xpath))).click()

    def selectVendor(self):
        select=Select(self.driver.find_element(By.XPATH,self.select_manOfVend_xpath))
        select.select_by_visible_text("Vendor 2")

    def clickChangePassword(self):
        self.driver.find_element(By.XPATH,self.rbtn_changepass_xpath).click()

    def clickSave(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()
