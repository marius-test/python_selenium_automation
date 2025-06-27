#  Consider the following HTML page source:
# What would be the MOST appropriate locator to use to locate the p element for the above page source?
#A. using XPATH ‘/html/body/div/div’
#B. Using the p element id
#C. Using the ClassName locator to be equal to ‘A4Q’
#D. Using the CSS selector ‘p.A4Q_’

# Answer: D


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


PATH = Service("C:\\Users\\marius\\webdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

file_path = "file:///C:/Users/marius/a4q_selenium/locators_training/locators_3.html"


driver.get(file_path)
p_element = driver.find_element(By.CSS_SELECTOR, 'body > div')
print(p_element.text)
time.sleep(5)
driver.quit()
