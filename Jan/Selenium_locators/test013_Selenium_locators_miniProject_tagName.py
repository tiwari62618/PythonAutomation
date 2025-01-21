import os
import time

from dotenv import load_dotenv
from requests import options
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



@allure.title("VWO Login Negative Testcase")
@allure.description("TC1 - Negative TC - VWO Login with invalid creds.")
@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():

    load_dotenv()
    chrome_options=Options()
    chrome_options.add_argument("--incognito")
    driver=webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))



    driver.quit() # close everything





