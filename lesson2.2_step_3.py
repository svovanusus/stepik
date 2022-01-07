import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

x_val = browser.find_element_by_id("num1").text
y_val = browser.find_element_by_id("num2").text

answer_select = Select(browser.find_element_by_id("dropdown"))
answer_select.select_by_value(str(int(x_val) + int(y_val)))

button = browser.find_element_by_css_selector("button.btn")
button.click()
