import math
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

x_val_el = browser.find_element_by_id("input_value")

answer_input = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
answer_input.send_keys(calc(x_val_el.text))

checkbox = browser.find_element_by_id("robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
checkbox.click()

radio = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()

button = browser.find_element_by_css_selector("button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
