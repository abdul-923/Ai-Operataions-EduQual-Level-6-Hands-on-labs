
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
alert_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Click for JS Confirm']")
    )
)

alert_button.click()
alert = WebDriverWait(driver, 10).until(
    EC.alert_is_present()
)
print("Alert says:", alert.text)
alert.dismiss()
print("Alert dismissed successfully.")
driver.quit()
