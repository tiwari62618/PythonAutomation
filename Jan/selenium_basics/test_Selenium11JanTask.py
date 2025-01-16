import time

from selenium import webdriver
import allure
import pytest

@allure.title("Verify that the title and current url of https://demo.us.espocrm.com/.")
@pytest.mark.regression
def test_():
   driver=webdriver.Chrome()
   driver.get("https://demo.us.espocrm.com/")
   time.sleep(10)
   print(driver.title)
   assert(driver.title=="EspoCRM Demo")
   print(driver.current_url)
   assert(driver.current_url=="https://demo.us.espocrm.com/")



