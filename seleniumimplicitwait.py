from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
driver.get(url)

line_count = 0
while True:
    chain = ActionChains(driver)
    chain.move_to_element(driver.find_element(By.CLASS_NAME, 'infinite-scroll'))
    chain.click()
    chain.send_keys([Keys.PAGE_DOWN for _ in range(100)])
    chain.perform()
    driver.implicitly_wait(10)
    result = driver.find_elements(By.CLASS_NAME, "quote")
    if line_count == len(result):
        break
    else:
        line_count = len(result)

print('Line Count:', len(result))
for item in result:
    print(item.text)

input('Please Enter a Key to Stop...')
driver.quit()
