# Given the following HTML document:
# Which of the following CSS selectors would correctly select the <a> tag inside the second <li> element?
# A) #menu li:nth-child(2) a
# B) #menu a:nth-of-type(2)
# C) li:nth-child(2) a
# D) #menu li a:nth-child(2)

# Answer: A


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


PATH = Service("C:\\Users\\marius\\webdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

file_path = "file:///C:/Users/marius/a4q_selenium/locators_training/locators_5.html"


driver.get(file_path)
element = driver.find_element(By.CSS_SELECTOR, '#menu > li:nth-child(2) > a')
print(element.text)
time.sleep(5)
driver.quit()
