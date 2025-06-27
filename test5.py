from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

PATH = Service(r"C:\Users\mariu\chromedriver.exe")
url = r"https://www.wikipedia.org/"
eng_link_locator = "js-link-box-en"
search_box_locator = "searchInput"
search_text = "Microsoft"

driver = webdriver.Chrome(service=PATH)
driver.get(url)
driver.maximize_window()

eng_link_element = driver.find_element(by=By.ID, value=eng_link_locator)
eng_link_element.click()

search_box_element = driver.find_element(by=By.ID, value=search_box_locator)
search_box_element.clear()
search_box_element.send_keys(search_text)
search_box_element.submit()

driver.quit()
