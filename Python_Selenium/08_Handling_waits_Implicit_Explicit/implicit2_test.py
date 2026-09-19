from selenium import webdriver

from selenium.webdriver.common.by import By

from pathlib import Path

driver = webdriver.Chrome()

html_file = Path("wait_test.html").resolve().as_uri()

driver.get(html_file)

driver.implicitly_wait(10)

element = driver.find_element(By.ID, "myButton")

print("Element found:", element.text)

driver.quit()
