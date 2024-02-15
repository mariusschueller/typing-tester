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

# waiting then clicking cookies popup
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'acceptAll'))).click()

# waiting for first word to appear
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.word.active')))

# getting the input element where text will be typed
inputSpace = driver.find_element(By.ID, 'wordsInput')

# infinite loop
while True:
    try:
        # checking if our results are hidden (will give error once test stops running cause result won't be hidden)
        driver.find_element(By.CSS_SELECTOR, "#result.hidden")

        # getting the active word
        active = driver.find_element(By.CSS_SELECTOR, '.word.active')

        # typing in the active word
        inputSpace.send_keys(active.text + " ")

    # catch error when one occurs
    except:
        print("Finished Typing")

        # exit the forever loop
        break

# final stats
print("I typed at "
      + driver.find_element(By.CSS_SELECTOR, '#result > div:nth-child(1) > div.group.wpm > div.bottom').text
      + " words per minute!")
