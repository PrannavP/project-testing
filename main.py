import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException

# importing credentials
from credentials import admin_email, admin_password

try:
    driver = webdriver.Chrome(executable_path='./chromedriver-win64/chromedriver.exe')

    driver.get('http://localhost/scms/pages/admin/admin-login.html')

    driver.implicitly_wait(10)

    try:
        driver.find_element_by_id('email').send_keys(admin_email)
        driver.find_element_by_id('psw').send_keys(admin_password)
        driver.find_element_by_id('admin-login').click()
    except NoSuchElementException:
        print("One of the elements was not found on the page.")
except WebDriverException as e:
    print(f"WebDriverException occurred: {e}")
finally:
    time.sleep(10)  # Wait for 10 seconds
    driver.quit()