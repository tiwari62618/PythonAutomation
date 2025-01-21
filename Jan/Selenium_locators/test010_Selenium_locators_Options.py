import time

from requests import options
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_katalon_chrome():

    chrome_options=Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    #chrome_options.add_argument("--window-size=900,600")
   # chrome_options.add_argument("--headless")


    driver=webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # 1. find the element the anchor tag
    # < a
    # id = "btn-make-appointment"
    # href = "./profile.php#login"
    # class ="btn btn-dark btn-lg"
    #  Make Appointment
    # < / a >
    make_appointment_element=driver.find_element(By.ID,"btn-make-appointment")
    # 2. click on it

    make_appointment_element.click()\

    # 3. verify that url changes
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(5)
    driver.quit() # close everything





