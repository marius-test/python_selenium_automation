# Same as exercise 3 with the implementation of a try catch construct. The automated test needs to be
# wrapped in a function named ‘login_to_saucedemo’ which will be called to execute the test.


# library imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# create a chrome driver instance
PATH = Service("C:\\Users\\marius\\webdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

# test data
url = "https://www.saucedemo.com/"
user_name = "standard_user"
password = "secret_sauce"


# test function definition
def login_to_saucedemo():
    # try to run the code
    try:
        # navigate to webpage
        driver.get(url)
        
        # find username box using xpath locator and enter username
        user_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        user_field.send_keys(user_name)
        
        # find password box using css selector and enter password
        password_field = driver.find_element(By.CSS_SELECTOR, '#password')
        password_field.send_keys(password)
        
        # find and click the login button
        driver.find_element(By.ID, 'login-button').click()
        
        # wait for the inventory container to be displayed
        wait = WebDriverWait(driver, 5)
        inventory_container = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'inventory_container')))
        
        # verify if login is successful and print the result
        if inventory_container.get_attribute("id") == "inventory_container":
                print("Login successful!")
        else:
                print("Login failed!")
    
    # handle the error
    except Exception as e:
        print(f"An error occurred: {type(e).__name__}")
    
    # cleanup/always run
    finally:
        # close the browser
        driver.quit()


# run the test
if __name__ == '__main__':
        login_to_saucedemo()
