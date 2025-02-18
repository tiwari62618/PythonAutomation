import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
import pytest

def test_check_radio_checkbox():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@id='sex-1']").click()
    time.sleep(3)
    driver.find_element(By.ID,"profession-1").click()
    time.sleep(3)
    driver.find_element(By.ID,"exp-2").click()
    time.sleep(3)