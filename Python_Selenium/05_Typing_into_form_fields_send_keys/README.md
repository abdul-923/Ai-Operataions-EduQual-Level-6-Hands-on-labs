
# Typing into Form Fields using Selenium

## Overview

This lab demonstrates how to automate typing into web form fields using Python and Selenium WebDriver.

A simple HTML webpage was created with username and password input fields. Selenium was used to open the webpage, locate the fields using their IDs, and enter text using the send_keys() method.

## Files Included

- test_page.html 
- send_keys_lab.py 
- README.md
- screenshots

## Commands Used

- cd ~/AI-Operations-EduQual-Level-6-Hands-on-labs/Python_Selenium
- mkdir Typing_into_Form_Fields_send_keys_lab
- cd Typing_into_Form_Fields_send_keys_lab
- source ../venv/bin/activate
- nano test_page.html
- nano send_keys_lab.py
- ls
- python3 send_keys_lab.py

## What I Learned

- How Selenium WebDriver controls Google Chrome.
- How to open a local HTML webpage using Selenium.
- How to locate webpage elements using their ID.
- How to use find_element() to locate input fields.
- How to use By.ID as a locator method.
- How to use send_keys() to type text into input fields.
- How Python and Selenium can automate repetitive web form tasks.
- How to verify successful execution through terminal output.

## Output

The Selenium script successfully opened the HTML webpage, located the username and password fields, and entered the required values.

Terminal output:

Element fields populated successfully.

The lab completed successfully and the browser was closed automatically.

## Conclusion

This lab provided practical experience with Selenium WebDriver and demonstrated how Python can automate interaction with web forms by locating input fields and entering text programmatically.
