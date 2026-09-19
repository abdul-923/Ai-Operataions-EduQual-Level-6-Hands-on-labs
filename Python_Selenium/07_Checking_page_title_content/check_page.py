
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.python.org")

page_title = driver.title
print(f"Page Title: {page_title}")

expected_title = "Welcome to Python.org"
assert page_title == expected_title, f"Title mismatch! Expected: {expected_title}, but got: {page_title}"

element = driver.find_element("xpath", "//a[text()='Downloads']")
actual_text = element.text
expected_text = "Downloads"

assert actual_text == expected_text, f"Text mismatch! Expected: {expected_text}, but got: {actual_text}"

print("Page title and Downloads text verified successfully.")

driver.quit()
