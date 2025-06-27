# Given the following HTML snippet, which of the following statements is TRUE regarding the <img> tag?
# A) The alt attribute is used to specify the width of the image.
# B) The width and height attributes define the actual size of the image file on the server.
# C) The alt attribute provides a text description of the image, which is important for accessibility.
# D) The src attribute is used to specify the alternative text for the image.

# Answer: C


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


PATH = Service("C:\\Users\\marius\\webdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

file_path = "file:///C:/Users/marius/a4q_selenium/locators_training/locators_1.html"


driver.get(file_path)
time.sleep(5)
driver.quit()
