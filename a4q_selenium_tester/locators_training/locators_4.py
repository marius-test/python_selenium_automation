#  Consider the following XML document:
# You need to extract all book titles from this XML document using an XPath expression. Which
# of the following XPath expressions would correctly return the titles of all books in the document?
# A) //book/booktitle
# B) //bookstore/book/name
# C) /bookstore/book/booktitles
# D) //booktitle/book

# Answer: A


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


PATH = Service("C:\\Users\\marius\\webdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

file_path = "file:///C:/Users/marius/a4q_selenium/locators_training/locators_4.html"


driver.get(file_path)
titles = driver.find_elements(By.XPATH, '//book/booktitle')
for title in titles:
    print(title.text)
time.sleep(5)
driver.quit()
