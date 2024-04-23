#This is the project of the Web  Automation in python


from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

# to open the chrome and wait for ten Second and close it.

# driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://www.google.com/")

# time.sleep(10)
# driver.close()


# to open the chrome and type something in the searsh bar and click search

driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com/")

search_bar= driver.find_element(By.ID,'APjFqb')

search_bar.send_keys("Sarkari Result")
# Search button
search_btn= driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')

search_btn.click()
#  Afte searching that key open the first link to open the website of the page
first_link= driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')
first_link.click()

#  Also searching the third link after the 
second_link= driver.find_element(By.XPATH,'//*[@id="wrap"]/ul/li[2]/a')
second_link.click()

time.sleep(100)
driver.close()

