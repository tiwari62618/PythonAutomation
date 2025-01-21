import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



def test_espocrm_click_login_button():

    load_dotenv()
    firefox_options=Options()
    #chrome_options.add_argument("--incognito")
    firefox_options.add_argument("--start-maximized")

    driver=webdriver.Firefox(firefox_options)
    driver.get(os.getenv("URL_ESPO"))
    time.sleep(10)

    #click on login button

    login_button=driver.find_element(By.ID,"btn-login")
    login_button.click()

    expected_url = "https://demo.us.espocrm.com/?l=en_US"
    assert driver.current_url==expected_url
    driver.quit()

    def test_espocrm_click_Advanced_pack():
        load_dotenv()
        chrome_options=Options()
        chrome_options.add_argument("--start-maximized")

        driver=webdriver.Chrome(chrome_options)
        driver.get(os.getenv("URL_ESPO"))
        time.sleep(10)
        advanced_pack_link=driver.find_element(By.LINK_TEXT,"Advanced Pack")
        advanced_pack_link.click()
        time.sleep(5)
        driver.quit()









    
