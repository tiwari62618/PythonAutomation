import time

import pytest
from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@allure.title("Alerts")
@allure.description("Verify JS Alerts")
def test_JS_alerts():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    element_prompt= driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    element_prompt.click()

    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())

    alert=driver.switch_to.alert
    alert.accept()

    result_text=driver.find_element(By.ID,"result").text
    assert result_text=="You successfully clicked an alert"

    time.sleep(5)

@allure.title("Alerts")
@allure.description("Verify JS Confirm")
def test_alert_confirm():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    element_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    element_confirm.click()

    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.dismiss()

    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You clicked: Cancel"

    time.sleep(5)

@allure.title("Alerts")
@allure.description("Verify JS Prompt")
def test_alert_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    element_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    element_confirm.click()

    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.send_keys("Pramod")
    alert.accept()

    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You entered: Pramod"

    time.sleep(5)

#native alerts selnium can't handle.