from selenium import webdriver
from selenium.webdriver.common.by import By
print('Implicit Wait...')
driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
driver.get(url)
for item in driver.find_elements(By.CLASS_NAME, "quote"):
    print(item.text)
input('Please Enter a Key to Stop...')
driver.quit()


