Lab 01 — Python Selenium: Launching a Browser and Opening a Web Page

Overview

- This lab introduces browser automation using Python and Selenium.
- It demonstrates how to launch Google Chrome, open a website automatically, retrieve the current URL, and close the browser.
- A Python virtual environment was used to install and run Selenium.

Files Included

- launch_browser.py
- test.py
- README.md
- Screenshots

Commands Used

- sudo apt install python3-venv
- python3 -m venv venv
- source venv/bin/activate
- pip install selenium
- python -c "import selenium; print(selenium.version)"
- google-chrome --version
- nano launch_browser.py
- python3 launch_browser.py

Python Code

- import time
- from selenium import webdriver
- driver = webdriver.Chrome()
- driver.get("https://www.mindrecalls.com")
- current_url = driver.current_url
- print(f"Current URL: {current_url}")
- time.sleep(15)
- driver.quit()

Screenshots

- Screenshot 1 — Python virtual environment and Selenium installation.
- Screenshot 2 — Selenium and Google Chrome version verification.
- Screenshot 3 — Selenium browser automation and URL output.
- Screenshot 4 — launch_browser.py created and edited using Nano.

Output

- Selenium was installed successfully.
- Google Chrome was launched automatically.
- Mind Recalls website was opened successfully.
- The current URL was retrieved and displayed in the terminal.
- The browser remained open for 15 seconds before closing.

Key Concepts Learned

- Python Selenium
- Selenium WebDriver
- Browser Automation
- Chrome WebDriver
- Python Virtual Environments
- pip Package Installation
- Webpage Navigation
- URL Retrieval
- Browser Control


What I Learned

- How to create and activate a Python virtual environment.
- How to install Selenium using pip.
- How to import Selenium WebDriver in Python.
- How to launch Chrome using Selenium.
- How to navigate to a webpage using driver.get().
- How to retrieve the current URL using driver.current_url.
- How to control the browser with Python.
- How to keep the browser open temporarily using time.sleep().
- How to close the browser using driver.quit().
