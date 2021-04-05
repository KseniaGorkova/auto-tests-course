from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    num = int(x)
    num2 = int(y)
    z = num + num2
    a = str(num+num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(a).click()
  
      
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
    print(x)
    print(y)
    print(a)
