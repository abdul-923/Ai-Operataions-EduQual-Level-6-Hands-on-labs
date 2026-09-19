
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.mindrecalls.com")

wait = WebDriverWait(driver, 10)

element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))

print("Element found:", element.text)

driver.quit()
