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


employee_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Employee List']")))
employee_list.click()

first_employee = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='oxd-icon bi-pencil-fill'])[2]")))
first_employee.click()

# Edit employee
first_name_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='firstName']")))
time.sleep(5)
# first_name_field.clear()
time.sleep(5)
first_name_field.send_keys("Updated")

last_name_field = driver.find_element(By.XPATH, "//input[@name='lastName']")
time.sleep(2)

time.sleep(2)
last_name_field.send_keys("Updated")

save_button = driver.find_element(By.XPATH, "//button[@type='submit']")
save_button.click()

time.sleep(5)
print("Employee details updated successfully!")


# Close the browser
driver.quit()