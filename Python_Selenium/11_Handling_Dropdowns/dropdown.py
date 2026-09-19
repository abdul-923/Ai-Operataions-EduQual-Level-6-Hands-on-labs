from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pathlib import Path

driver = webdriver.Chrome()

html_file = Path("dropdown.html").resolve()
driver.get(html_file.as_uri())

dropdown = driver.find_element(By.ID, "dropdown-example")

select_element = Select(dropdown)

select_element.select_by_visible_text("Option 2")

selected_option = select_element.first_selected_option
print("Selected option:", selected_option.text)

select_element.select_by_value("3")

selected_option = select_element.first_selected_option
print("Selected option:", selected_option.text)

driver.quit()
