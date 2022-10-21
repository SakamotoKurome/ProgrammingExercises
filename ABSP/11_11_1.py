from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get('https://www.guerrillamail.com/compose')
message = '''
Hello World!
This is the first mail by using ptyhon selenium.
'''
elems = browser.find_elements(By.CLASS_NAME, 'form-field')
# To
elems[0].send_keys('mobij19563@lutota.com')
# Subjects
elems[1].send_keys('Hello World')
elems[2].send_keys(message)
elems[2].submit()
browser.quit()
