from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

try:
    # Wait for elements to appear
    driver.implicitly_wait(10)

    # Open website
    driver.get("https://www.automationexercise.com/")

    print("Page title:", driver.title)

    # Wait for Products link and click it
    products_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[href="/products"]')
        )
    )

    products_button.click()

    print("Products page opened.")

    # Wait for Products page to load
    WebDriverWait(driver, 10).until(
        EC.url_contains("/products")
    )

    print("Current URL:", driver.current_url)

    # Take screenshot
    screenshot = driver.save_screenshot("screenshot.png")

    print("Screenshot saved:", screenshot)

    # Validate page
    assert "/products" in driver.current_url

    print("Validation successful.")

finally:
    driver.quit()

print("Test completed successfully.")
