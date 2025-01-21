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

    # 1. Find the email and enter the wrong username or email
    # <input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >

    email_web_element=driver.find_element(By.ID,"login-username")
    email_web_element.send_keys(os.getenv("INVALID_USERNAME"))

    # 2. Find the password and enter the wrong password
    # <input
    # type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    # data-gtm-form-interact-field-id="1">

    password_web_element=driver.find_element(By.ID,"login-password")
    password_web_element.send_keys(os.getenv("INVALID_PASSWORD"))

    # <button
    # type="submit"
    # id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica">

    submit_button=driver.find_element(By.ID,"js-login-btn")
    submit_button.click()

    # Wait for sometime
    time.sleep(5)

    # <div
    # class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">
    # Your email, password, IP address or location did not match
    # </div>

    error_msg_web_element=driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error_msg_web_element.text)

    assert error_msg_web_element.text==os.getenv("error_message_expected")

    time.sleep(5)
    driver.quit() # close everything





