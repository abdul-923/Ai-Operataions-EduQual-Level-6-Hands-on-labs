
# Lab 03 — Locating Elements by CSS Selector and XPath

## Overview

This lab demonstrates how to locate web elements using **CSS Selectors** and **XPath** with Python Selenium.

A simple HTML test page was created with username and password input fields. Selenium was then used to open the page and locate the username input element using two different methods.

The lab helps build a practical understanding of how Selenium identifies specific elements on a webpage before performing actions such as typing, clicking, or submitting forms.

## Files Included

- test_page.html 
- css_selector.py 
- xpath.py 
- Screenshots
- Readme 

## Environment

- Operating System: Ubuntu
- Programming Language: Python
- Automation Tool: Selenium
- Browser: Google Chrome
- Python Virtual Environment: venv

## Commands Used

- Activate the existing virtual environment.
- Install Selenium:

pip install selenium

- Run the CSS Selector script:

python3 css_selector.py

- Run the XPath script:

python3 xpath.py

## Python Code

### CSS Selector

The CSS Selector script opens the HTML page and locates the username input using:

#username

The # symbol means that Selenium is looking for an element with the ID username.

The script then prints the element tag and ID to verify that the correct element was found.

### XPath

The XPath script opens the same HTML page and locates the username input using:

//*[@id="username"]

This XPath tells Selenium to find an element whose ID attribute is username.

WebDriverWait was also used to wait until the element was available before trying to locate it.


## Output

### CSS Selector Output

Element found using CSS Selector!

Tag: input

ID: username

### XPath Output

Element found using XPath!

Tag: input

ID: username

## Key Concepts Learned

- How Selenium opens a webpage using Chrome WebDriver.
- How Selenium locates elements on a webpage.
- What a CSS Selector is.
- How to use an ID as a CSS Selector.
- What XPath is.
- How to locate an element using XPath.
- How to verify a located element using tag_name and get_attribute().
- How WebDriverWait can wait for an element to become available.
- The difference between CSS Selector and XPath.
- How element locating forms the foundation of browser automation.

## What I Learned

In this lab, I learned that Selenium needs a way to identify specific elements on a webpage before it can interact with them.

I practiced two common locating methods: CSS Selectors and XPath.

The CSS Selector #username and XPath //*[@id="username"] were both used to locate the same username input element.

This lab provided a practical foundation for future Selenium automation tasks such as entering usernames and passwords, clicking buttons, submitting forms, and navigating websites automatically.
