from selenium.webdriver import ChromeOptions
from splinter import Browser
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from halo import Halo

likestool_user = 'XXXX'
likestool_pass = 'XXXX'
max_work = 60


def likestool_login(browser):
    browser.visit('https://likestool.com/site/login')
    sleep(1)
    browser.fill('LoginForm[username]', likestool_user)
    browser.fill('LoginForm[password]', likestool_pass)
    browser.find_by_xpath('//*[@id="login_form"]/div[4]/input').click()
    sleep(5)


def likestool_work(browser, page):
    url = 'https://likestool.com/campaign/{}'.format(page)
    browser.visit(url)
    for x in range(max_work):
        coins = browser.find_by_css('#coins').text
        msg = '{}: {} points / {}'.format(x, coins, page)
        spinner.text = msg
        go = False
        while not go:
            try:
                browser.find_by_css('.campaign_button.bg_red').click()
                if page == 'DAILYMOTION_VIEWS':
                    sleep(12)
                    browser.windows.current = browser.windows[1]
                    browser.execute_script("document.getElementById('dmp_Video').pause();")
                    browser.windows.current = browser.windows[0]
                    sleep(33)
                else:
                    sleep(45)
                go = True
            except Exception:
                browser.reload()
        sleep(randint(7, 15))


spinner = Halo(text='Booting up...', spinner='dots')
spinner.start()

chrome_options = ChromeOptions()
chrome_options.add_argument('--autoplay-policy=user-gesture-required')

with Browser('chrome', headless=True, incognito=True, options=chrome_options) as browser:
    likestool_login(browser)
    likestool_work(browser, 'YOUTUBE_VIEWS')
    likestool_work(browser, 'DAILYMOTION_VIEWS')
    likestool_work(browser, 'SOUNDCLOUD_LISTEN')
