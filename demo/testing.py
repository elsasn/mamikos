from gettext import install

import pip
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

print("sample test case started")
driver = driver=webdriver.Chrome(r"/Users/user/PycharmProjects/mamikos/Browser/chromedriver")
#driver=webdriver.firefox()
#driver=webdriver.ie()
#maximize the window size
driver.maximize_window()
#navigate to the url
driver.get("https://www.google.com/")
#identify the Google search text box and enter the value
driver.find_element_by_name("q").send_keys("javatpoint")
time.sleep(3)
#click on the Google search button
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(3)
#close the browser
driver.close()
print("sample test case successfully completed")