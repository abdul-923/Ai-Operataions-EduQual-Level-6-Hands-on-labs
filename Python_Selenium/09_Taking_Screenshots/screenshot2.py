
from selenium import webdriver
from datetime import datetime
import time
driver = webdriver.Chrome()
driver.get("https://www.mindrecalls.com")
print("Waiting for the page to load...")
time.sleep(15)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
screenshot_name = f"youtube_screenshot_{timestamp}.png"
driver.save_screenshot(screenshot_name)
print(f"Screenshot saved as: {screenshot_name}")
driver.quit()
