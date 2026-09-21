
# Python Selenium Lab 09 — Taking Screenshots

## Overview

Today I successfully performed Lab 10 on taking screenshots using Python and Selenium WebDriver.

In this lab I opened a real website using Selenium and captured a screenshot after allowing the page to load. I also used timestamps in the screenshot filename to keep the files organized.

## Files Included

* README.md
* screenshot.py
* screenshot2.py
* youtube_screenshot_20260919_151449.png
* youtube_screenshot_20260919_153451.png

## Commands Used

* source venv/bin/activate
* mkdir 09_Taking_Screenshots
* cd 09_Taking_Screenshots
* nano screenshot.py
* nano screenshot2.py
* python3 screenshot.py
* python3 screenshot2.py
* ls

## Output

* Selenium successfully opened YouTube.
* The page was given 15 seconds to load.
* Selenium successfully captured the webpage screenshot.
* Screenshots were saved as PNG files.
* Timestamped filenames were created successfully.

## What I Learned

* How to take screenshots using Selenium.
* How to use driver.save_screenshot().
* How to wait before taking a screenshot.
* How to use Python time.sleep().
* How to generate timestamps using datetime.
* How to create timestamped screenshot filenames.
* How to verify the generated screenshot files.

## Conclusion

Today I successfully completed the Selenium screenshot lab. I practiced opening a real website and automatically capturing its current browser view. I also learned how to add timestamps to screenshot filenames and save multiple screenshots without overwriting previous files.
