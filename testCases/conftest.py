import platform

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):

    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver=webdriver.Edge()
    else:
        service = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        driver.implicitly_wait(5)
    return driver

def pytest_addoption(parser):  #This will get the Browser from cmd line
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   #This will pass the Browser to setup
    return request.config.getoption("browser")

# pytest -v -s -n=2 path.file.py --browser edge  --> to run multiple test at a time

#************ PyTest HTML Report******************
def pytest_html_report_title(report):
    report.title = "NopCommerce Test Report"
