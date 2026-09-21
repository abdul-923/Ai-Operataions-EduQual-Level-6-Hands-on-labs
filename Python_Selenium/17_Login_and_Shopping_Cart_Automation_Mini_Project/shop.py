
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")

username.send_keys("standard_user")

password = driver.find_element(By.ID, "password")

password.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")

login_button.click()

WebDriverWait(driver, 10).until(

EC.url_contains("inventory.html")

)

assert "inventory.html" in driver.current_url

print("Login successful.")

product = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")

product.click()

print("Product added to cart.")

cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")

cart.click()

cart_product = WebDriverWait(driver, 10).until(

EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))

)

assert cart_product.text == "Sauce Labs Backpack"

print("Product verified in cart.")

driver.save_screenshot("shopping_cart.png")

print("Screenshot saved successfully.")

driver.quit()

print("Test completed successfully.")
