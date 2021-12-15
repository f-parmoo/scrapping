from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://www.webscrapingfordatascience.com/complexjavascript/')
explicit_wait_driver = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'quote')))

for item in explicit_wait_driver:
    print(item.text)
