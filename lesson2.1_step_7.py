import math
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

x_val_el = browser.find_element_by_id("treasure")

answer_input = browser.find_element_by_id("answer")
answer_input.send_keys(calc(x_val_el.get_attribute("valuex")))

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()

radio = browser.find_element_by_id("robotsRule")
radio.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
