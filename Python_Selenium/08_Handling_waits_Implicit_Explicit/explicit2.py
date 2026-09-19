from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from pathlib import Path

driver = webdriver.Chrome()

html_file = Path("wait_test.html").resolve().as_uri()

driver.get(html_file)

wait = WebDriverWait(driver, 10)

element = wait.until(

EC.visibility_of_element_located((By.ID, "myButton"))

)

print("Element found and visible:", element.text)

driver.quit()
