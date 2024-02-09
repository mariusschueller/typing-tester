from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Opening mokeytype")

driver = webdriver.Chrome()
driver.get('https://monkeytype.com/')

# get the thing with two classes
time.sleep(5)

driver.find_element(By.CLASS_NAME, 'acceptAll').click()

active = driver.find_element(By.CSS_SELECTOR, '.word.active')
print(active.text)

inputSpace = driver.find_element(By.ID, 'wordsInput')

print(inputSpace)

inputSpace.send_keys(active.text + " ")
time.sleep(1)

active = driver.find_element(By.CSS_SELECTOR, '.word.active')
print(active.text)

# driver.find_element(By.ID,"CouncilDistInput").send_keys("1408 18th Avenue South, Nashville, TN")

time.sleep(10)
# closing the driver
driver.close()
