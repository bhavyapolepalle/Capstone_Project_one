from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


driver.maximize_window()
driver.implicitly_wait(10)


username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("Admin")


password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin123")


login_button = driver.find_element(By.XPATH, "//*[@type='submit']")
login_button.click()


time.sleep(5)


wait = WebDriverWait(driver, 10)
pim_module = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
pim_module.click()

time.sleep(5)
employee_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Employee List']")))
employee_list.click()


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
first_employee = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='oxd-icon bi-trash'])[3]")))
time.sleep(5)
first_employee.click()
time.sleep(5)
confirm_delete_button = driver.find_element(By.XPATH, "//*[@class='oxd-icon bi-trash oxd-button-icon']")
time.sleep(5)
confirm_delete_button.click()


time.sleep(10)
print("Employee details are deleted successfully")


# Close the browser
driver.quit()