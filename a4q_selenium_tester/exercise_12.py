"""
Reporting functionalities will now be added to the result of exercise 11.
pytest-html will be used for test logging and reporting.

The tests to be logged onto the report are as below:
    1) Navigate to Website
    2) Verify the page title
    3) Login on Website
    4) Verify Product Filter

An HTML report should be produced with the main test case being “test_login_to_saucedemo”. Under
this test case, there should then be the individual test steps of navigation, page title verification, login,
and product filter verification.
Pytest fixtures are to be used for the report. One fixture is to setup the report configuration and the
second fixture is for the web driver configuration.

Note:
    1) Run pip install pytest-html in PyCharm Terminal to install the libraries needed for pytest-html in
    the project.
    2) To generate the html report, run the command below in the PyCharm Terminal in the correct
    folder:
    pytest <script name> --html=report.html

For example: in the directory
“C:\\Users\\User\\PycharmProjects\\pyTestAutomation\\Python Exercises>” in the
PyCharm Terminal, run the below command:
pytest Exercises.py --html=report.html
"""


# library imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


# test data
url = "https://www.saucedemo.com/"
user_name = "standard_user"
password = "secret_sauce"


# pytest configuration
@pytest.fixture(scope='session', autouse=True)
def setup_reporting():
    config = {
    'report_title': 'Test Report for Saucedemo',
    'output_file': 'report.html'
    }
    return config
@pytest.fixture(scope='function')
def driver():
    PATH = Service("C:\\Users\\marius\\webdriver\\chromedriver.exe")
    driver = webdriver.Chrome(service=PATH)
    yield driver


# test function definition
def test_login_to_saucedemo(setup_reporting, driver):
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


# to execute the test, run the following command from the terminal 'pytest exercise_12.py --html=report.html'
