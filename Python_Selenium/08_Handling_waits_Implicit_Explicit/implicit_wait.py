
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.mindrecalls.com")

driver.implicitly_wait(12)

element = driver.find_element(By.TAG_NAME, "h3")

print("Element found:", element.text)

driver.quit()
