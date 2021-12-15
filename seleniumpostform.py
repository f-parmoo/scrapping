from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.webscrapingfordatascience.com/postform2/')

driver.find_element(By.NAME, 'name').send_keys('David')
driver.find_element(By.CSS_SELECTOR, 'input[name="gender"][value="M"]').click()
driver.find_element(By.NAME, 'pizza').click()
driver.find_element(By.NAME, 'salad').click()
Select(driver.find_element(By.NAME, 'haircolor')).select_by_value('brown')
driver.find_element(By.NAME, 'comments').send_keys('Hello', Keys.ENTER, 'How are you?', Keys.ENTER, 'Whats up')
input('Please Enter a key for submitting form')
driver.find_element(By.TAG_NAME, 'form').submit()
input('Please Enter a key for exiting')
driver.quit()
