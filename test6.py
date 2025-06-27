from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

PATH = Service(r"C:\Users\mariu\chromedriver.exe")
url = r"https://www.wikipedia.org/"
language_locators = ["js-link-box-en", "js-link-box-fr", "js-link-box-de"]
search_box_locator = "searchInput"
search_text = "Microsoft"
wait_time = 5

driver = webdriver.Chrome(service=PATH)
driver.get(url)
wait = WebDriverWait(driver, wait_time)
# driver.implicitly_wait(5)
driver.maximize_window()

for i in range(len(language_locators)):
    # language_link = driver.find_element(by=By.ID, value=language_locators[i])
    language_link = wait.until(expected_conditions.presence_of_element_located((By.ID, language_locators[i])))
    language_link.click()
    # search_box_element = driver.find_element(by=By.ID, value=search_box_locator)
    search_box_element = wait.until(expected_conditions.presence_of_element_located((By.ID, search_box_locator)))
    search_box_element.clear()
    search_box_element.send_keys(search_text)
    search_box_element.submit()
    time.sleep(5)
    driver.back()
    driver.back()
  
