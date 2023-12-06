from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get("https://gmail.com")

user = driver.find_element_by_id("identifierId")
user.send_keys("Myemail@gmail.com")
user.send_keys(Keys.ENTER)
time.sleep(3)

password = driver.find_element_by_name("password")
password.send_keys("mypassword")
password.send_keys(Keys.ENTER)

