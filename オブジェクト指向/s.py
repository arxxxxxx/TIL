import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from datetime import datetime

import collections
import time
from timeout_decorator import timeout,TimeoutError

import pyperclip

l = ['ランチョンマット',' エキスパート','ポニョ','チュッパチャップス','マツキヨ','プレイステーション','クリームパン','伊藤園',' ハイボール',' 日傘',' アイアンマン','ブロンズ像','缶バッジ']
yugiou = 'いちご ギフト 大國屋'
r = 1
y = 1
ipArray = []

@timeout(30)
def check1():
    sleep(10)
    x,y = pyautogui.locateCenterOnScreen('rakuten-search.png',grayscale=True)
    print(x,y)

@timeout(30)
def check2():
    sleep(10)
    # x,y = pyautogui.locateCenterOnScreen('check.png',grayscale=True)
    # print(x,y)

def rakuten(i):
    global r
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('network.proxy.type', 1)
    firefox_profile.set_preference('network.proxy.socks', '127.0.0.1')
    firefox_profile.set_preference('network.proxy.socks_port', 9150)

    browser = webdriver.Firefox(firefox_profile=firefox_profile)

    browser.get("https://www.rakuten.co.jp/")
    sleep(60)

    wait = WebDriverWait(browser, 120) # 最大120秒

    try:
        elem = wait.until( expected_conditions.element_to_be_clickable( (By.ID,"sitem")) )
        elem = browser.find_element_by_id("sitem")
        sleep(30)
        elem.send_keys(yugiou, Keys.RETURN)
        sleep(30)
        pyautogui.screenshot('%s.png' % datetime.now())
        print('rakuten %s' % r)
        sleep(30)
        browser.close()
        browser.quit()
        r += 1
    except:
        print('rakuten error')
        browser.close()
        browser.quit()

def yahoo(i):
    global y
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('network.proxy.type', 1)
    firefox_profile.set_preference('network.proxy.socks', '127.0.0.1')
    firefox_profile.set_preference('network.proxy.socks_port', 9150)

    browser = webdriver.Firefox(firefox_profile=firefox_profile)

    browser.get("https://shopping.yahoo.co.jp/")
    sleep(60)

    wait = WebDriverWait(browser, 120) # 最大120秒

    try:
        elem = wait.until( expected_conditions.element_to_be_clickable( (By.ID,"ss_yschsp")) )
        elem = browser.find_element_by_id("ss_yschsp")
        sleep(30)
        elem.send_keys(yugiou, Keys.RETURN)
        sleep(30)
        pyautogui.screenshot('%s.png' % datetime.now())

        print('yahoo %s' % y)
        sleep(30)
        browser.close()
        browser.quit()
        y += 1
    except:
        print('yahoo error')
        browser.close()
        browser.quit()

def check33():
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('network.proxy.type', 1)
    firefox_profile.set_preference('network.proxy.socks', '127.0.0.1')
    firefox_profile.set_preference('network.proxy.socks_port', 9150)

    browser = webdriver.Firefox(firefox_profile=firefox_profile)

    # ipアドレスチェック
    browser.get("https://www.cman.jp/network/support/go_access.cgi")
    global ipArray
    wait = WebDriverWait(browser, 120) # 最大120秒
    try:
        elem = wait.until( expected_conditions.element_to_be_clickable( (By.CLASS_NAME,"outIp")) )
        elem = browser.find_element_by_class_name("outIp").text
        ipArray.append(elem)
        pyautogui.screenshot('%s.png' % datetime.now())
        browser.close()
        browser.quit()
    except:
        print('error')
        browser.close()
        browser.quit()

def main():
    i = 0
    #  len(l) or (r <= len(l) and y <= len(l))
    while True:
        sleep(30)
        # rakuten
        # now = datetime.now()
        # print(now)

        # pyautogui.moveTo(985,75,0.5)
        # pyautogui.click(985,75)

        # pyautogui.moveTo(806,148,0.5)
        # pyautogui.click(806,148)

        # sleep(10)

        # pyautogui.moveTo(330,77,0.5)
        # pyautogui.click(330,77)

        # pyperclip.copy('https://www.rakuten.co.jp/')
        # # pyautogui.click(834,157)
        # pyautogui.hotkey('command', 'v')
        # pyautogui.press('enter')

        # sleep(30)
        # try:
        #     check1()
        # except TimeoutError:
        #     j = 0
        #     print('timeout')
        #     sleep(30)
        #     continue

        # pyautogui.moveTo(228,174,0.5)
        # pyautogui.click(228,174)

        # pyperclip.copy(l[i])
        # pyautogui.hotkey('command', 'v')
        # pyautogui.press('enter')

        # sleep(30)
        # try:
        #     check2()
        # except TimeoutError:
        #     j = 0
        #     print('timeout')
        #     sleep(30)
        #     # continue
        #     j = 1
        # else:
        #     j = 1
        #     pyautogui.screenshot('%s.png' % datetime.now())

        # pyautogui.moveTo(985,75,0.5)
        # pyautogui.click(985,75)

        # pyautogui.moveTo(806,148,0.5)
        # pyautogui.click(806,148)
        # ipアドレスチェック
        check33()
        print(ipArray)
        print(collections.Counter(ipArray))
        # rakuten
        sleep(60)
        if(r < 100):
                rakuten(i)
        sleep(60)
        # yahoo
        if(y < 100):
                yahoo(i)
        i += 1
        sleep(180)

if __name__ == "__main__":
        main()
