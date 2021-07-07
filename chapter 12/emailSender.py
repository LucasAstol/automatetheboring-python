#! python3
# emailSender.py - sends an email to a given email address with the given text with the credentials provided

import re, sys, time
from selenium import webdriver

if len(sys.argv) == 5:
    userEmail = sys.argv[1]
    userPass = sys.argv[2]
    destEmail = sys.argv[3]
    emailText = sys.argv[4]

    browser = webdriver.Firefox()
    browser.get('https://mail.google.com/mail/u/0/#inbox')
    browser.find_element_by_id('identifierId').send_keys(userEmail)
    browser.find_element_by_css_selector('#identifierNext button').click()
    browser.implicitly_wait(10)
    time.sleep(5)
    browser.find_element_by_css_selector('#password input').send_keys(userPass)
    browser.find_element_by_css_selector('#passwordNext button').click()
    time.sleep(5)
    browser.find_element_by_css_selector("div[id=':3a'] div[role='button']").click()
    time.sleep(5)
    browser.find_element_by_css_selector("form[method='POST'] textarea[role='combobox']").send_keys(destEmail)
    browser.find_element_by_css_selector("input[name='subjectbox']").send_keys('My subject')
    browser.find_element_by_css_selector("#undefined div[role='textbox']").send_keys(emailText)
    browser.find_element_by_css_selector('div[data-tooltip="Send ‪(Ctrl-Enter)‬"]').click()
    print('Email sent')
else:
    print('please enter arguments correctly, 1-user email, 2-user pass, 3-destination email, 4-email body')