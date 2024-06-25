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
password_field.send_keys("admin123")


login_button =driver.find_element(By.XPATH, "//*[@type='submit']")
login_button.click()

# Wait for a few seconds to ensure the login process completes
time.sleep(5)


try:
    dashboard_element = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
    print("Login successful!")


    pim_module = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
    pim_module.click()


    time.sleep(2)

    add_employee_button = driver.find_element(By.XPATH,
                                              '//*[@class="oxd-icon bi-plus oxd-button-icon"]')
    add_employee_button.click()


    time.sleep(2)

    # Step 6: Fill in the employee details
    first_name_field = driver.find_element(By.NAME, "firstName")
    first_name_field.send_keys("test")

    middle_name_field = driver.find_element(By.NAME, "middleName")
    middle_name_field.send_keys("T")

    last_name_field = driver.find_element(By.NAME, "lastName")
    last_name_field.send_keys("now")

    employee_id_field = driver.find_element(By.XPATH,
                                            '(//*[@class="oxd-input oxd-input--active"])[2]')
    employee_id_field.clear()
    employee_id_field.send_keys("1234")


    save_button = driver.find_element(By.XPATH, '//*[@type="submit"]')
    save_button.click()

    # Wait for a few seconds to ensure the employee is added
    time.sleep(5)

    print("New employee added successfully!")

except Exception as e:
    print("An error occurred:", e)

# Close the browser
driver.quit()