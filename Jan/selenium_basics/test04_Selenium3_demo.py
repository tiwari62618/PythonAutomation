import time

from selenium import webdriver
import allure
import pytest

@allure.title("open the app.vwo.com")
@pytest.mark.regression
def test_vwo_sample_selenium_3():
    driver_path='"C:\Users\mohit\Downloads\edgedriver_win64\msedgedriver.exe"'
    driver=webdriver.EdgeService(executable_path=driver_path)
    driver.get("https://app.vwo.com")
    #This code is translated into api request
    #it will become a post request that will go to browser driver(server)
   # where it will create a session or fresh copy browser(chrome)
    #Session Id-16 digit (dadeqdaf3232q) will be created

    driver.get("https://app.vwo.com")
    #Get -> Get api request to navigate to particular page.
    #browser will navigate to the url.
    #source code(client)-> Api request(w3c protocol) -> browser Driver(Server)->Browser
    print(driver.session_id)

    driver.get("https://app.vwo.com")
    time.sleep(10)