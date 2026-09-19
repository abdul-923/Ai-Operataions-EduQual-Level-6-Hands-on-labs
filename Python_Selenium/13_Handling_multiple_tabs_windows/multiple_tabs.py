
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path

driver = webdriver.Chrome()
html_file = Path("test_page.html").resolve()
driver.get(html_file.as_uri())
link = driver.find_element(By.LINK_TEXT, "Open Python in New Tab")
link.click()

window_handles = driver.window_handles

print("Total open windows/tabs:", len(window_handles))

for handle in window_handles:
 driver.switch_to.window(handle)
 print("Window handle:", handle)
 print("Title:", driver.title)
 print("URL:", driver.current_url)
 print("--------------------")
driver.quit()
