
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path

driver = webdriver.Chrome()
html_file = Path("index.html").resolve()
driver.get(html_file.as_uri())

print("Main page opened.")
iframes = driver.find_elements(By.TAG_NAME, "iframe")
print(f"Total iFrames found: {len(iframes)}")
driver.switch_to.frame("exampleFrame")
print("Switched to iFrame successfully.")
button = driver.find_element(By.ID, "submitButton")
button.click()
print("Button inside iFrame clicked successfully.")
driver.switch_to.default_content()
print("Switched back to main page successfully.")

driver.quit()
