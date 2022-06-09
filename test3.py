from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

PATH = Service("C:\\Users\\mariu\\geckodriver.exe")
driver = webdriver.Firefox(service=PATH)

driver.get("https://the-internet.herokuapp.com/")
time.sleep(5)

link = driver.find_element(by=By.LINK_TEXT, value="A/B Testing")
link.click()

time.sleep(5)
driver.quit()
