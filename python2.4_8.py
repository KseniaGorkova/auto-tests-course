from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
    butt = browser.find_element_by_id("book")
    butt.click()
    
    browser.execute_script("window.scrollBy(0, 200);")
    
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    b = browser.find_element_by_id("solve")
    b.click()
finally:
    time.sleep(30)
    browser.quit()