from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

input("Press Enter to close...")

driver.quit()
