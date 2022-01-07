import os
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

inputs = browser.find_elements_by_css_selector("input[type=\"text\"][required]")
for inp in inputs:
    inp.send_keys("Some Text")

dirpath = os.path.abspath(os.path.dirname(__file__))
filepath = os.path.join(dirpath, "file.txt")

print(filepath)

file_el = browser.find_element_by_id("file")
file_el.send_keys(filepath)

button = browser.find_element_by_css_selector("button.btn")
button.click()
