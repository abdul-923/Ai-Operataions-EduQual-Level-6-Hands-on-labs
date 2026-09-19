
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path

driver = webdriver.Chrome()

html_file = Path("form.html").resolve()

driver.get(html_file.as_uri())

name_field = driver.find_element(By.ID, "name")
email_field = driver.find_element(By.ID, "email")

name_field.send_keys("John")
email_field.send_keys("john@example.com")

submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

print("Form submitted successfully!")

input("Press Enter to close the browser...")

driver.quit()
