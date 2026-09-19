
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.python.org")

print("Waiting for the page to load...")
time.sleep(5)

links = driver.find_elements(By.TAG_NAME, "a")

print(f"Total number of links found: {len(links)}")
print("\nLinks found:")

for link in links:
 text = link.text
href = link.get_attribute("href")

if text:
    print(f"Text: {text}")
    print(f"URL: {href}")
    print("-" * 50)

driver.quit()
