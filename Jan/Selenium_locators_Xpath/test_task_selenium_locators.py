# Open the Url - www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067
# Search for the Macmini
# Click on the search ICON
# Get all the titles
# Get al the prices
# Print all the titles and prices in the end.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_print_titles_prices_macmini():
    driver=webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    time.sleep(5)
    search_box_input=driver.find_element(By.XPATH,"//input[@title='Search']")
    search_box_input.send_keys("Macmini")

    search_box_button=driver.find_element(By.XPATH,"//span[@class='gh-search-button__label']")
    search_box_button.click()

    list_of_items=driver.find_elements(By.CSS_SELECTOR,".s-item__title")
    list_of_items_prize=driver.find_elements(By.CSS_SELECTOR,".s-item__price")

    for items in list_of_items:
        print(items.text)
    print(len(list_of_items))

    for items_prize in list_of_items_prize:
        print(items_prize.text)
    print(len(list_of_items_prize))


