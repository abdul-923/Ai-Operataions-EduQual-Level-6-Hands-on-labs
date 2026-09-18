
from selenium import webdriver

from selenium.webdriver.common.by import By

from pathlib import Path

driver = webdriver.Chrome()

html_file = Path("test_page.html").resolve()

driver.get(html_file.as_uri())

username_field = driver.find_element(By.ID, "username")

username_field.send_keys("testuser")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("securepassword123")
print("Username and password fields populated successfully.")
driver.quit()
