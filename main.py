from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

print("Opening monkeytype.com")
driver.get('https://monkeytype.com/')

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'acceptAll'))).click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.word.active')))

inputSpace = driver.find_element(By.ID, 'wordsInput')

while True:
    try:
        driver.find_element(By.CSS_SELECTOR, "#result.hidden")
        active = driver.find_element(By.CSS_SELECTOR, '.word.active')
        inputSpace.send_keys(active.text + " ")

    except:
        print("Finished Typing")
        break

print("I typed at "
      + driver.find_element(By.CSS_SELECTOR, '#result > div:nth-child(1) > div.group.wpm > div.bottom').text
      + " words per minute!")
