from _ast import Assert

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


driver.maximize_window()
driver.implicitly_wait(10)

username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("Admin")


password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("Invalid password")


login_button = driver.find_element(By.XPATH, "//*[@type='submit']")
login_button.click()


time.sleep(5)


print("Invalid credentials !!!")



