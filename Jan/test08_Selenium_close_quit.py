import time

from selenium import webdriver
import allure
import pytest

@allure.title("Verify that the title of vwo.com is expected.")
@pytest.mark.regression

def test_katalon_firefox_close():
    driver=webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(10)
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
    driver.close()

def test_katalon_firefox_quit():
    driver=webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(10)
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
    driver.quit()





