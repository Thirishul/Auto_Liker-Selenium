from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
import time


class twitterbot:
    def __init__(self, user, pas):
        self.user = user
        self.pas = pas
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(10)
        email = bot.find_element_by_name('session[username_or_email]')
        pas = bot.find_element_by_name('session[password]')
        email.clear()
        pas.clear()
        email.send_keys(self.user)
        pas.send_keys(self.pas)
        pas.send_keys(keys.RETURN)
        time.sleep(10)

    def like(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=typed')
        time.sleep(10)
        for i in range(0, 2):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            tweets = bot.find_elements_by_class_name('css-4rbku5')
            links = [elem.get_attribute('href')
                     for elem in tweets]
            for link in links:
                bot.get('https://twitter.com/' + link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(4)
                except Exception as ex:
                    time.sleep(50)


sul = twitterbot('GMAIL-ID', 'PASSWORD')
sul.login()
sul.like('RAJINI')

#MADE BY THIRISHUL ASOKAN