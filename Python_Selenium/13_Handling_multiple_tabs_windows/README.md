
# Python Selenium Lab 13 — Handling Multiple Windows/Tabs

## Overview

Today I successfully performed this lab on handling multiple browser tabs and windows using Python Selenium.

In this lab I created a local web page with a link that opens Python.org in a new tab. I used Selenium to detect both open tabs and switch between them.

I also extracted the window handles along with the title and URL of each tab.

## Files Included

* README.md
* multiple_tabs.py
* test_page.html
* Screenshots

## Commands Used

* cd ~/AI-Operations-EduQual-Level-6-Hands-on-labs/Python_Selenium
* source venv/bin/activate
* mkdir 13_Handling_multiple_tabs_windows
* cd 13_Handling_multiple_tabs_windows
* nano test_page.html
* google-chrome test_page.html
* nano multiple_tabs.py
* python3 multiple_tabs.py
* ls

## What I Learned

* How Selenium handles multiple browser tabs
* How to open a new tab using a link
* How to get all open window handles
* How to use driver.window_handles
* How to switch between tabs using driver.switch_to.window()
* How to get the title of the current tab
* How to get the URL of the current tab
* How to use a for loop with window handles
* How Selenium identifies different browser tabs

## Output

* Total open windows/tabs: 2
* Selenium successfully detected both tabs
* The first tab showed the title First Page
* The first tab showed the local HTML file URL
* The second tab opened Python.org
* Selenium successfully switched between the available tabs
* Window handles for both tabs were displayed successfully

## Conclusion

Today I successfully performed and completed the lab on handling multiple browser windows and tabs using Python Selenium.

I practiced opening a new tab and getting the window handles of both tabs. I also learned how Selenium switches between tabs and extracts information such as the page title and URL.

This lab helped me understand how Selenium manages multiple browser tabs during web automation.
