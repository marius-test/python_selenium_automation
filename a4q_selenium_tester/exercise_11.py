# Same as exercise 10 except that when the test is completed, the time taken for the test to be executed is
# displayed in milliseconds.


# library imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# create a chrome driver instance
PATH = Service("C:\\Users\\marius\\webdriver\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

# test data
url = "https://www.saucedemo.com/"
user_name = "standard_user"
password = "secret_sauce"


# test function definition
def login_to_saucedemo():
    # start time for the test
    start = time.time()
    
    # try to run the code
    try:
        # navigate to webpage
        driver.get(url)
        
        # wait for the webpage to load completely
        time_limit = 180
        while driver.execute_script("return document.readyState") != "complete" and time_limit < 180:
            time.sleep(1)
            time_limit += 1
        
        # hard assertion for page title
        title = driver.title
        assert title == "Swag Labs", f"Assertion Fail: Title is not Swag Labs, it is {title}."
        print("Assertion Pass: Title is Swag Labs.")
                
        # find username box using id locator and enter username
        user_field = driver.find_element(By.ID, 'user-name')
        user_field.send_keys(user_name)
        
        # find password box using the locate with and below methods
        password_field = driver.find_element(locate_with(By.TAG_NAME, 'input').below({By.ID:'user-name'}))  # overcomplicated way to locate an element
        password_field.send_keys(password)
        
        # find and click the login button
        driver.find_element(By.ID, 'login-button').click()
        
        # wait for the inventory container to be displayed
        wait = WebDriverWait(driver, 10)
        inventory_container = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'inventory_container')))
        
         # verify if login is successful and print the result
        if inventory_container.get_attribute("id") == "inventory_container":
                print("Login successful!")
                
                # soft assertion for product filter
                try:
                    product_filter = driver.find_element(By.CLASS_NAME, "product_sort_container")  # locate the product filter
                    assert product_filter.is_displayed(), "Product filter is not displayed."  # assert is a built-in Python function; is_displayed() is a Selenium function
                    print("Assertion Pass: Product filter is displayed.")
                except AssertionError as e:
                    print(str(e))

                # screenshots the third shop item with its description and add to cart button
                driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[3]').screenshot("inventory_3.png")
                
                # alternatively
                """inventory_item = driver.find_element(By.XPATH, ".//*[@class='inventory_item'][3]")
                screenshot = inventory_item.screenshot_as_png
                with open("inventory_3.png", "wb") as file:
                    file.write(screenshot)"""
                    
        else:
                print("Login failed!")
    
    # handle the error
    except Exception as e:
        print(f"An error occurred: {type(e).__name__}")
    
    # cleanup/always run
    finally:
        # close the browser
        driver.quit()
        
        # end time for the test
        end = time.time()
        
        # calculate and display test execution time in milliseconds
        print(f"Test duration is: {(end - start) * 1000:.2f} ms.")


# run the test
if __name__ == '__main__':
        login_to_saucedemo()
