import math
import time
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

button = browser.find_element_by_css_selector("button.btn")
button.click()

browser.switch_to.alert.accept()
time.sleep(1)

x_val = browser.find_element_by_id("input_value").text

answer = browser.find_element_by_id("answer")
answer.send_keys(calc(x_val))

button = browser.find_element_by_css_selector("button.btn")
button.click()
