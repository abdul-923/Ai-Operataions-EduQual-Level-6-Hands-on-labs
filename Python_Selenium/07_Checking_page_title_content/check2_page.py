import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://mindrecalls.com/")
time.sleep(15)
page_title = driver.title
print(f"Page Title: {page_title}")

expected_title = "Mind Recalls – Crack Your MRCPsych Exam with Our High-Yield, Syllabus-Aligned MCQ Banks Collected Straight From Recent Exam Candidates. Repeated Questions, Clear Explanations and with Money-Back Guarantee"
assert page_title == expected_title, f"Title mismatch! Expected: {expected_title}, but got: {page_title}"

element = driverelement = driver.find_element("xpath", "//a[contains(normalize-space(.), ' Start Course Now')]")

actual_text = element.text
expected_text = " Start Course Now"

assert actual_text == expected_text, f"Text mismatch! Expected: {expected_text}, but got: {actual_text}"

print("Page title and Course text verified successfully.")

driver.quit()
