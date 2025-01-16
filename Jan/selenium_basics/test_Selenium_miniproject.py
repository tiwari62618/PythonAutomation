import time

from selenium import webdriver
import allure
import pytest

@allure.title("Verify that the title of vwo.com is expected.")
@pytest.mark.regression
def test_vwo_sample():
    driver=webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "PURA Healthcare Service" in driver.page_source:
        print("Text found, Test case passed")
    else:
        print("Text not found on the page")
        pytest.fail("Text not found on the page")



