# Lab 8: Checking Page Title & Content

## Overview

Today I successfully performed the Selenium lab for checking a webpage title and webpage content.

In this lab, I used Python and Selenium WebDriver to open a webpage, read its page title, verify the expected title, locate an element on the page, and compare its actual text with the expected text.

I also tested the script with the Mind Recalls website to understand how Selenium handles real webpage content and element validation.

## Files Included

* check2_page.py
* check_page.py
* Screenshot of terminal output
* Screenshot of webpage
* README.md

## Commands Used

* cd ~/AI-Operations-EduQual-Level-6-Hands-on-labs/Python_Selenium
* source venv/bin/activate
* mkdir "07_Checking_page_title_contents"
* cd "07_Checking_page_title_contents"
* nano check2_page.py
* python3 check2_page.py
* ls

## What I Learned

* How to use Selenium WebDriver with Python
* How to open a webpage using Selenium
* How to retrieve a webpage title using driver.title
* How to store webpage information in Python variables
* How to use assert to verify expected results
* How to locate webpage elements using XPath
* How to read the text of a webpage element
* How Selenium reports a failed assertion
* How Selenium reports NoSuchElementException when an element cannot be located
* How automated testing compares actual webpage data with expected data
* How to close the browser using driver.quit()

## Output

The Selenium script successfully opened the Mind Recalls website and retrieved its actual page title.

The title was displayed in the terminal and compared against the expected title.

The element validation was also tested. The test showed an assertion error when the text returned by Selenium did not match the expected text.

This helped me understand how Selenium identifies and validates webpage elements.


## Conclusion

Today I successfully performed the Selenium lab for checking page title and webpage content.

I learned how Python and Selenium can be used to automatically open a webpage, read its title, locate elements, retrieve their text, and verify whether the actual webpage content matches the expected result.

I also learned how automated tests identify mismatches and report errors when the webpage does not contain the expected content.

This lab gave me a better understanding of how Selenium can be used for basic web automation and webpage testing.
