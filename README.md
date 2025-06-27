# python_selenium_automation

**Selenium** automation demos in **Python**

Libraries: *selenium, time*

This project contains five Selenium scripts showcasing different browser automation techniques using Chrome and Firefox WebDrivers.

### Scripts overview

0. **basic_chrome_launch.py**  
   Launches Chrome and opens a URL.

1. **search_techwithtim.py**  
   Performs a search on `techwithtim.net`, waits for results, prints article summaries, and closes the browser.

2. **navigate_links.py**  
   Navigates through links on `techwithtim.net`, clicks buttons, and demonstrates browser navigation (back/forward).

3. **firefox_ab_testing.py**  
   Opens Firefox, navigates to a test page, clicks a link, then closes the browser.

4. **cookie_clicker_bot.py**  
   Automates clicks on the Cookie Clicker game using Firefox, demonstrates implicit waits, and item upgrades with action chains.

5. **wikipedia_search.py**  
   Opens Wikipedia, selects the English language, searches for "Microsoft", and then closes the browser.

6. **multi_language_wikipedia_search.py**  
   Opens Wikipedia, iterates through English, French, and German languages, performs a search for "Microsoft" in each, waits between actions, and navigates back after each search.

---

### A4Q Selenium Tester

The `a4q_selenium_tester` folder contains my solutions to the **A4Q Certified Selenium 4 Tester Foundation v3.0** workshop exercises, completed as part of my certification preparation, which I successfully passed in May 2025.

The goal is to validate and demonstrate my skills as a **Selenium Automation Tester** by completing the official workshop exercises and passing the certification exam.

#### Contents

- Completed solutions to the official **A4Q Selenium Tester Foundation Workshop Exercises** (Python)
- `locators_training` contains my locator solutions; the exercises are based on examples from the official mock exam

---

### Page Object Model

The `page_object_model` folder contains a Selenium test case implemented using the Page Object Model pattern, featuring:

- `element.py`: Descriptor class handling input elements with explicit waits.
- `locator.py`: Centralized locators for page elements.
- `page.py`: Page classes representing web pages, encapsulating actions and verifications.
- `main.py`: Test case using `unittest` framework that searches on python.org, demonstrating POM in action.

---

### Tech Stack

- **Python** - core programming language  
- **Selenium** - browser automation framework  
- **ChromeDriver** - Chrome WebDriver for automation  
- **unittest** and **pytest** - test framework

---

### Notes

- ChromeDriver path is hardcoded; update `PATH` variable to match your local setup.  
- Scripts use explicit and implicit waits to handle page load timing.  
- This was my first Selenium learning project and helped me build a solid foundation for more advanced automation work.
