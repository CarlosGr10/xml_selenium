from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get("http://python.org")
driver.close()



