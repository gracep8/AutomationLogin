from lib2to3.pgen2 import driver
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://facebook.com")
driver.find_element_by_xpath("//input[@class = 'inputtext _55r1 _6luy']").send_keys("gpakasi8888@gmail.com")
driver.find_element_by_xpath("//input[@class = 'inputtext _55r1 _6luy _9npi']").send_keys("22iippii")

link = driver.find_element_by_xpath("//button[@class = '_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']").click()

time.sleep(20)
driver.quit()
