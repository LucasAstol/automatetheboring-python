#! python3
# seleniumExample.py - just example of selenium

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('cover-thumb')   
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Element not found')