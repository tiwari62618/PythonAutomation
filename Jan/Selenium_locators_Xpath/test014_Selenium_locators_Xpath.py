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


    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_app_btn=driver.find_element(By.XPATH,"//a[text()='Make Appointment' and contains(@id,btn-make-appointment)]")
    make_app_btn.click()
    time.sleep(5)

    driver.quit() # close everything





