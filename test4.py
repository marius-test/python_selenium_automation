from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

PATH = Service("C:\\Users\\mariu\\geckodriver.exe")
driver = webdriver.Firefox(service=PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(5)

english = driver.find_element(by=By.ID, value="langSelect-EN")
english.click()

# got_it = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/a[1]")
# got_it.click()

cookie = driver.find_element(by=By.ID, value="bigCookie")
cookie_count = driver.find_element(by=By.ID, value="cookies")

items = [driver.find_element(by=By.ID, value="productPrice" + str(i)) for i in range(1, -1, -1)]

for i in range(5000):
    actions = ActionChains(driver)
    actions.click(cookie)
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
