
# Python Selenium Lab 10 — Locating Multiple Elements

## Overview

Today I successfully performed Lab 11 on locating multiple elements using Python and Selenium WebDriver.

In this lab I opened Python.org and used Selenium to find all hyperlinks on the webpage. I counted the total number of links and extracted the visible text and URL of each link.

## Files Included

* README.md
* multiple_elements.py

## Commands Used

* cd ~/AI-Operations-EduQual-Level-6-Hands-on-labs/Python_Selenium
* source venv/bin/activate
* mkdir 10_Locating_Multiple_Elements
* cd 10_Locating_Multiple_Elements
* nano multiple_elements.py
* python3 multiple_elements.py
* ls
* pwd

## Output

* Python.org was opened successfully using Selenium.
* Selenium found 223 links on the webpage.
* The links were processed one by one.
* The visible text of each link was displayed.
* The URL of each link was extracted.
* The Privacy Notice link was successfully displayed with its URL.

## What I Learned

* How to locate multiple elements using Selenium.
* How to use find_elements().
* How to locate elements using By.TAG_NAME.
* How the HTML a tag represents hyperlinks.
* How to count elements using len().
* How to loop through multiple elements.
* How to get visible text using link.text.
* How to get URLs using get_attribute().
* How Selenium can be used for basic web scraping.

## Conclusion

Today I successfully completed the Selenium lab on locating multiple elements. I practiced finding all hyperlinks on a real webpage and processing them one by one. This helped me understand the difference between finding a single element and finding multiple elements using Selenium.
