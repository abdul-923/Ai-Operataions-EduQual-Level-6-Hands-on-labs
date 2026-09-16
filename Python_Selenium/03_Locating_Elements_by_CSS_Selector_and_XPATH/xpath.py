
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
driver = webdriver.Chrome()
html_file = Path("test_page.html").resolve()
driver.get(html_file.as_uri())
username_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
)
print("Element found using XPath!")
print("Tag:", username_element.tag_name)
print("ID:", username_element.get_attribute("id"))
driver.quit()
