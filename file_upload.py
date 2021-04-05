import time
import os
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    
    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys('Vasa')
    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys('Lolola')
    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys('Lol@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'bio.txt')
    element = browser.find_element_by_id('file')
    element.send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
    
