from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

html_file = Path("test_page.html").resolve().as_uri()
driver.get(html_file)

time.sleep(2)

username_element = driver.find_element(By.ID, "username")

print("Element with ID 'username':", username_element.get_attribute("outerHTML"))

time.sleep(5)
driver.quit()
