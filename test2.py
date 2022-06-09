from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

time.sleep(10)
driver.maximize_window()

driver.get("https://www.techwithtim.net/")

link = driver.find_element(by=By.LINK_TEXT, value="Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id=\"sow-button-19310003\"]"))
    )
    element.click()

    driver.back()  # goes back on the previous webpage
    driver.forward()  # goes forward on the next webpage

except:
    driver.quit()
