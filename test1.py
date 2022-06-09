from selenium import webdriver  # no need to explain this one
from selenium.webdriver.common.by import By  # for find_element function
from selenium.webdriver.common.keys import Keys  # for pressing keyboard buttons
from selenium.webdriver.support.wait import WebDriverWait  # for waiting on a webpage until something is located
from selenium.webdriver.chrome.service import Service  # to import chromedriver.exe
from selenium.webdriver.support import expected_conditions as EC  # the expected condition for the wait
import time  # so we can make the code to sleep

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

driver.get("https://www.techwithtim.net")
print(driver.title)

search = driver.find_element(by=By.NAME, value="s")
search.clear()
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    print(main.text)
    articles = main.find_element(by=By.TAG_NAME, value="article")
    for article in articles:
        header = article.find_element(by=By.CLASS_NAME, value="entry-summary")
        print(header.text)
finally:
    time.sleep(5)
    driver.quit()
