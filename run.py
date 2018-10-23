from splinter import Browser
from bs4 import BeautifulSoup
from random import randint
from halo import Halo
import time


likestool_user = 'XXXX'
likestool_pass = 'XXXX'
max_work = 60


def likestool_login(browser):
    browser.visit('https://likestool.com')
    time.sleep(1)
    browser.fill('LoginForm[username]', likestool_user)
    browser.fill('LoginForm[password]', likestool_pass)
    browser.find_by_xpath('//*[@id="login_form"]/input[2]').click()
    time.sleep(5)


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
                time.sleep(45)
                go = True
            except Exception:
                browser.reload()
        time.sleep(randint(7, 15))


def slumber():
    t = time.localtime()
    t = time.mktime(t[:3] + (0, 0, 0) + t[6:])
    t = t + 24 * 3600 - time.time()
    time.sleep(t)


spinner = Halo(text='Booting up...', spinner='dots')
spinner.start()

with Browser(headless=True, incognito=True, profile_preferences={'media.volume_scale': '0.0', 'media.autoplay.enabled': False, 'permissions.default.image': 2}) as browser:
    likestool_login(browser)
    while 1:
        likestool_work(browser, 'DAILYMOTION_VIEWS')
        likestool_work(browser, 'YOUTUBE_VIEWS')
        slumber()
