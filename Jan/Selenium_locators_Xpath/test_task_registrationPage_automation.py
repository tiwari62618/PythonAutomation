#Automation for the Registration Page of the AwesomeQA.com/UI
# Open - https://awesomeqa.com/ui/index.php?route=account/register
#
# Fill the form
#
# Verify that next page give - Your Account Has Been Created!
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_registration_page_automate():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    first_name_input=driver.find_element(By.CSS_SELECTOR,"#input-firstname")
    first_name_input.send_keys("Mohit")

    last_name_input = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
    last_name_input.send_keys("Tiwari")

    email_input = driver.find_element(By.CSS_SELECTOR, "#input-email")
    email_input.send_keys("tiwari234@gmail.com")

    telephone_input = driver.find_element(By.CSS_SELECTOR, "input[type='tel']")
    telephone_input.send_keys("9876567463")

    password_input = driver.find_element(By.CSS_SELECTOR, "#input-password")
    password_input.send_keys("m12345")

    confirm_password_input = driver.find_element(By.CSS_SELECTOR, "#input-confirm")
    confirm_password_input.send_keys("m12345")

    radiobutton_select = driver.find_element(By.XPATH, "//input[@type='radio' and @value='0']")
   # radiobutton_select = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='0']")
    radiobutton_select.click()

    checkbox_select = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    checkbox_select.click()

    continue_button_click = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    continue_button_click.click()

    time.sleep(4)

    text_Successful_msg="Your Account Has Been Created!"
    assert driver.find_element(By.XPATH,"//h1[text()='Your Account Has Been Created!']").text==text_Successful_msg
    time.sleep(4)




