from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


# user input message id, ex: messenger.com/t/123123232.. Type only the number.
message_to = input('message ID: ')

# user input facebook login number.
number = str(input('login number: '))

# user input facebook login password
pwd = str(getpass("login password: "))

# type the message to send
message = str(input("type what to send: "))

# open the chrome browser
driver = webdriver.Firefox()
driver.maximize_window()

# goto messenger.com
driver.get('https://m.me')
time.sleep(2)

# log in with given info
driver.find_element_by_xpath('//*[@id="email"]').click()
driver.find_element_by_xpath('//*[@id="email"]').send_keys(number)

driver.find_element_by_id("pass").send_keys(pwd)
driver.find_element_by_id('loginbutton').click()
time.sleep(2)

# finding the given inbox
driver.get(f'https://messenger.com/t/{message_to}')

# sending the message
driver.switch_to_active_element().send_keys(message)
time.sleep(1)
driver.switch_to_active_element().send_keys(Keys.ENTER)
time.sleep(3)

# done and quitting the browser
driver.quit()