# a .py file I usually create for all my projects to quickly debug and test any part of my program
# it can also serve as a template


# import unittest
# import urllib3
# import requests
# import pyautogui
# import seletools
import time
# import unittest
# from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.relative_locator import locate_with
# from selenium.common.exceptions import TimeoutException
# from webdriver_manager.chrome import ChromeDriverManager


PATH = Service("C:\\Users\\marius\\webdriver\\chromedriver.exe")
# if using webdriver_manager lib, it can handle downloading/updating chromedriver automatically
# chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=PATH)

url = "https://amionline.net/"


driver.get(url)
time.sleep(5)
