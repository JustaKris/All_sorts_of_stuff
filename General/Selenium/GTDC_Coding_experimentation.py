import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initializing Chrome
chrome = webdriver.Chrome('C://Users//kristiyan.bonev//Desktop//stuff//Selenium drivers//chromedriver')
chrome.get('http://nuex-wwsafep01.gfk.com/ops/prod/#/processing')

# Tolerable delay
chrome.implicitly_wait(10)
chrome.set_page_load_timeout(10)
chrome.maximize_window()

# Login page
username = chrome.find_element_by_class_name('md-input')
username.send_keys(os.environ.get('OPS_USER'))

password = chrome.find_element_by_id('pwInput')
password.send_keys(os.environ.get('OPS_PASS'))
# Improvised delay
password.click()
password.click()
password.click()
password.send_keys(Keys.ENTER)

# Home page
coding_button = chrome.find_element_by_xpath('//a[@href="#/coding"]')
coding_button.click()

coding_searchbar = chrome.find_element_by_xpath('//div[@class="md-select md-theme-default"]')
coding_searchbar.click()

# GTDC = chrome.find_element_by_xpath("//*[text()='GTDC Processor Model']")

chrome.get('http://nuex-wwsafep01.gfk.com/ops/prod/#/coding?config=1011')

# chrome.find_element_by_css_selector('input[value=oneway]') # How to select using css_selector
# chrome.quit()
