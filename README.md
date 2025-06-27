# python_selenium_automation

**Selenium** automation demos in **Python 3**

Libraries: *selenium, time*

This project contains five Selenium scripts showcasing different browser automation techniques using Chrome and Firefox WebDrivers.

### Scripts overview

1. **basic_chrome_launch.py**  
   Launches Chrome and opens a URL.

2. **search_techwithtim.py**  
   Performs a search on `techwithtim.net`, waits for results, prints article summaries, and closes the browser.

3. **navigate_links.py**  
   Navigates through links on `techwithtim.net`, clicks buttons, and demonstrates browser navigation (back/forward).

4. **firefox_ab_testing.py**  
   Opens Firefox, navigates to a test page, clicks a link, then closes the browser.

5. **cookie_clicker_bot.py**  
   Automates clicks on the Cookie Clicker game using Firefox, demonstrates implicit waits, and item upgrades with action chains.

---

### Notes

- ChromeDriver and GeckoDriver paths are hardcoded; update `PATH` variables to match your local setup.  
- Scripts use explicit and implicit waits to handle page load timing.  
- This was my first Selenium learning project—an enjoyable introduction that paved the way for more advanced automation projects.

