from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


# Facebook profile/group name to send message.
message_to = input('Message to: ')

# user input facebook login number.
number = str(input('Login number: '))

# user input facebook login password
pwd = str(getpass("Login password: "))

# type the message to send
message = str(input("Type the message: "))

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
time.sleep(3)

# finding the Users given inbox
driver.find_element_by_css_selector('#js_w > div > div > div._1nq2._7vup > span._5iwm._6-_b._150g._58ah > label > input').click()
driver.find_element_by_css_selector('#js_w > div > div > div._1nq2._7vup > span._5iwm._6-_b._150g._58ah > label > input').send_keys(message_to)
driver.find_element_by_css_selector('#js_w > div > div > div._1nq2._7vup > span._5iwm._6-_b._150g._58ah > label > input').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/div/div/div[2]/ul/li/a/div/div[2]/div').click()
time.sleep(2)



# sending the message
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div').click()
driver.switch_to_active_element().send_keys(message)
time.sleep(1)
driver.switch_to_active_element().send_keys(Keys.ENTER)
time.sleep(3)

# done and quitting the browser
driver.quit()