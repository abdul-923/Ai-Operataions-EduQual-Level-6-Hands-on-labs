
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import time
driver = webdriver.Chrome()
html_file = Path("test_page.html").resolve()
driver.get(html_file.as_uri())
button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "sampleButton"))
)
print("Button found!")
print("Tag:", button.tag_name)
print("ID:", button.get_attribute("id"))
button.click()
result = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "result"))
)
print("Button clicked successfully!")
print("Result:", result.text)
time.sleep(3)
driver.quit()
