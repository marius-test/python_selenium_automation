# Consider the following HTML snippet from a webpage:
# Which locator strategy would be MOST effective for identifying the "Buy Now" button for
# Product A in this scenario?
# A) Use XPath to target the <button> element by its index and position within the product-list class.
# B) Use id="product1" to target the <div> element, and then use cssSelector to locate the button within that div.
# C) Use cssSelector to locate the button element by its class buy-btn and the data-product-id="1" attribute.
#D) Use XPath to target the button element by its class buy-btn and inner text "Buy Now" for all buttons.

# Answer: D


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


PATH = Service("C:\\Users\\marius\\webdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

file_path = "file:///C:/Users/marius/a4q_selenium/locators_training/locators_7.html"


driver.get(file_path)
button_1 = driver.find_element(By.CSS_SELECTOR, "#product1 > button")
print(button_1.text)
time.sleep(5)
driver.quit()
