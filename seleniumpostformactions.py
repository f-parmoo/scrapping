from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.webscrapingfordatascience.com/postform2/')

chain = ActionChains(driver)

chain.send_keys_to_element(driver.find_element(By.NAME, 'name'), 'David')
chain.click(driver.find_element(By.CSS_SELECTOR, 'input[name="gender"][value="M"]'))
chain.click(driver.find_element(By.NAME, 'pizza'))
chain.click(driver.find_element(By.NAME, 'salad'))
Select(driver.find_element(By.NAME, 'haircolor')).select_by_value('brown')
chain.send_keys_to_element(driver.find_element(By.NAME, 'comments'), 'Hello', Keys.ENTER, 'How are you?', Keys.ENTER,
                           'Whats up')
chain.perform()
input('Please Enter a key for submitting form')
driver.find_element(By.TAG_NAME, 'form').submit()
input('Please Enter a key for exiting')
driver.quit()
