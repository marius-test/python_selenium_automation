#  Given the following XML document, which of the following XPath expressions will select
# all the author elements of books that were published after the year 2000?
# A) /library/book[year>2000]/title
# B) //book[year>2000]/author
# C) /library/book/author[year>2000]
# D) //book[year>2000][author]

# Answer: B


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


PATH = Service("C:\\Users\\marius\\webdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

file_path = "file:///C:/Users/marius/a4q_selenium/locators_training/locators_2.html"


driver.get(file_path)
authors = driver.find_elements(By.XPATH, '//book[year>2000]/author')
for author in authors:
    print(author.text)
time.sleep(5)
driver.quit()
