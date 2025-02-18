import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtables_rows_columns():
    driver=webdriver.Firefox()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()

    rows_elements=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    total_rows=len(rows_elements)
    print("total rows are :- "+ str(total_rows) )

    column_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[1]/th")
    total_columns = len(column_elements)
    print("total columns are :- " + str(total_columns))

    time.sleep(4)
    driver.quit()





