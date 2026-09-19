
# Python Selenium Lab 12 — Handling Alerts

## Overview

Today I successfully performed Lab 12 on Handling Alerts using Python and Selenium WebDriver.

In this lab I practiced working with JavaScript alerts in a web browser. I learned how to trigger an alert and switch Selenium to the alert so I could interact with it.

I practiced accepting an alert and dismissing a confirmation alert. I also retrieved and printed the alert text.

## Files Included

* alerts.py
* accept_alert.py
* dismiss_alert.py
* README.md
* Screenshots

## Commands Used

* cd ~/AI-Operations-EduQual-Level-6-Hands-on-labs/Python_Selenium
* source venv/bin/activate
* mkdir 12_Handling_Alerts
* cd 12_Handling_Alerts
* nano alerts.py
* python3 alerts.py
* mv alerts.py accept_alert.py
* nano dismiss_alert.py
* python3 dismiss_alert.py
* ls

## What I Learned

* How JavaScript alerts work
* How to trigger an alert using Selenium
* How Selenium switches to an alert
* How to use switch_to.alert
* How to read alert text
* How to accept an alert
* How to dismiss an alert
* How to use WebDriverWait
* How to use alert_is_present()
* How to close the browser using driver.quit()

## Output

### Accept Alert

Alert says: I am a JS Alert

Alert accepted successfully.

### Dismiss Alert

Alert says: I am a JS Confirm

Alert dismissed successfully.

Both alert handling scripts ran successfully.

## Conclusion

Today I successfully performed the Selenium Handling Alerts lab.

I practiced triggering JavaScript alerts and interacting with them using Selenium. I learned how to switch to an alert and then accept or dismiss it.

This lab helped me understand how Selenium can automate browser pop-ups and handle JavaScript alerts during web automation testing.
