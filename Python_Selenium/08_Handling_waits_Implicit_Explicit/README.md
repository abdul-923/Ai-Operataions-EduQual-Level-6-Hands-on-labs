# Python Selenium Lab 8 — Handling Waits

## Overview

Today I successfully performed Lab 9 on Handling Waits using Python and Selenium WebDriver.

In this lab I worked with implicit waits and explicit waits. I created a local HTML page where a button appeared after a short delay and tested how Selenium waits for the element.

This lab helped me understand how Selenium handles elements that are not immediately available.

## Files Included

* README.md
* implicit_wait.py
* implicit2_test.py
* explicit_wait.py
* explicit2.py
* wait_test.html
* Screenshots

## Commands Used

* cd ~/AI-Operations-EduQual-Level-6-Hands-on-labs/Python_Selenium
* source venv/bin/activate
* mkdir 08_Handling_Waits
* cd 08_Handling_Waits
* nano wait_test.html
* nano implicit_wait.py
* nano implicit2_test.py
* nano explicit_wait.py
* nano explicit2.py
* python3 implicit_wait.py
* python3 implicit2_test.py
* python3 explicit_wait.py
* python3 explicit2.py
* ls
* pwd
* cat wait_test.html
* grep myButton wait_test.html

## What I Learned

* How implicit waits work in Selenium
* How explicit waits work in Selenium
* How to use driver.implicitly_wait()
* How to use WebDriverWait
* How to use expected_conditions
* How to wait for an element to become visible
* How Selenium handles dynamic elements
* How to use find_element()
* How to use By.ID
* How to understand NoSuchElementException
* How to check and fix a local HTML file path
* The difference between general waiting and condition based waiting

## Output

### Implicit Wait

Element found: Click Me

### Explicit Wait

Element found and visible: Click Me

Both scripts successfully found the button.

The main difference was how Selenium was instructed to wait for the element.

## Conclusion

Today I successfully performed the Selenium Handling Waits lab.

I practiced both implicit and explicit waits using a local HTML page and a dynamically appearing button.

I also faced and fixed errors during the lab which helped me better understand element searching and waiting in Selenium.

This lab gave me a better understanding of how Selenium handles dynamic web pages and how waits can make browser automation more reliable.

