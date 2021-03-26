import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
import time

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    
    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
      
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()