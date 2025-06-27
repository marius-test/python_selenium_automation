# Write a Python program using Selenium libraries that opens a Google Chrome browser,
# navigate to “https://www.saucedemo.com/” and closes the browser.


# library imports
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# create a chrome driver instance
PATH = Service("C:\\Users\\marius\\webdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

# test data
url = "https://www.saucedemo.com/"

# navigate to webpage
driver.get(url)

# wait 5 seconds
time.sleep(5)

# close the browser
driver.quit()
