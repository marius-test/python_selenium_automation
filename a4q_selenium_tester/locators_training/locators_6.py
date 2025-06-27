# Given the following XML document:
# Which of the following XPath expressions would select the <name> of all products that
# belong to the "Electronics" category and cost more than 20?
# A) //product[category='Electronics' and price>20]/name
# B) //product[name='Electronics' and price>20]/name
# C) //product[category='Electronics']/name
# D) //product[price>20]/name

# Answer: A


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


PATH = Service("C:\\Users\\marius\\webdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

file_path = "file:///C:/Users/marius/a4q_selenium/locators_training/locators_6.html"


driver.get(file_path)
products = driver.find_elements(By.XPATH, "//product[category='Electronics' and price>20]/name")
for product in products:
    print(product.text)
#time.sleep(5)
driver.quit()
