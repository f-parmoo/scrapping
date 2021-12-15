from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.webscrapingfordatascience.com/complexjavascript/')

quote_count = 0
while True:
    chain = ActionChains(driver)
    chain.move_to_element(driver.find_element(By.CLASS_NAME, 'infinite-scroll'))
    chain.click()
    chain.send_keys([Keys.PAGE_DOWN for _ in range(100)])
    chain.perform()

    result = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'quote')))
    if len(result) == quote_count:
        break
    else:
        quote_count = len(result)

print('Line Count:', len(result))
for item in result:
    print(item.text)

input('Please presss any ket to exit...')
driver.quit()
