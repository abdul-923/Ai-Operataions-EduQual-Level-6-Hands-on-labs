Lab 02 — Locating Elements by ID

Overview

- This lab introduced how Selenium locates specific HTML elements using their unique ID.
- A local HTML test page was created with username and password fields.
- Selenium was used to open the page, locate the username field by its ID, retrieve its HTML, and print the result.

Files Included

- README.md
- locate_by_id.py
- test_page.html
- Screenshots

Commands Used

- source ../venv/bin/activate
- nano test_page.html
- nano locate_by_id.py
- ls
- pwd
- grep -n "username" test_page.html
- cat locate_by_id.py
- python3 locate_by_id.py

Lab Tasks

- Created a simple HTML test page containing:
  - Username field
  - Password field
  - Login button
  
- Created a Python Selenium script named locate_by_id.py.
- Initialized the Chrome WebDriver.
- Opened the local HTML test page.
- Located the username input using its ID.
- Retrieved the element's outer HTML.
- Printed the result in the terminal.
- Closed the browser after execution.

Output

- Chrome opened successfully.
- The local test page loaded successfully.
- Selenium successfully located the username element.
- The terminal displayed:
  - Element with ID 'username': <input type="text" id="username" name="user_name">
- The browser closed successfully after the script completed.

Key Concepts Learned

- Selenium WebDriver
- HTML elements
- Element IDs
- Locating elements by ID
- By.ID locator
- Local HTML files
- Selenium element attributes
- Browser automation

What I Learned

- How to create a simple HTML page for Selenium testing.
- How to use Selenium with Python.
- How to locate an HTML element using its unique ID.
- How to retrieve an element's HTML attributes.
- How Selenium can identify and interact with specific elements on a webpage.
- How to use a shared Python virtual environment for multiple Selenium labs.
