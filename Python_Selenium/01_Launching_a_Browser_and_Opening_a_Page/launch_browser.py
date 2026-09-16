
import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.mindrecalls.com")

current_url = driver.current_url
print(f"Current URL: {current_url}")

time.sleep(15)

driver.quite()
