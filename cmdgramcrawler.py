from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from bs4 import BeautifulSoup



class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(5)
        username = bot.find_element_by_name('username')
        username.send_keys(self.username)
        password = bot.find_element_by_name('password')
        password.send_keys(self.password)
        username = bot.find_element_by_name('username')
        username.send_keys()
        password = bot.find_element_by_name('password')
        password.send_keys()
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        clicker = bot.find_element_by_css_selector('button.aOOlW.HoLwm')
        clicker.send_keys(Keys.RETURN)



harvey = InstaBot(os.environ.get('USER'),os.environ.get('PASS'))
harvey.login()
key = Keys()
