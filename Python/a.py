import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from random import randint

from datetime import datetime

import collections
import time
# from timeout_decorator import timeout,TimeoutError

# import pyperclip


l = ['ランチョンマット',' エキスパート','ポニョ','チュッパチャップス','マツキヨ','プレイステーション','クリームパン','伊藤園',' ハイボール',' 日傘',' アイアンマン','ブロンズ像','缶バッジ']
data1 = 'マンゴー贈答用'
data1rakuten = 'マンゴー 宮崎 大國屋'
data2 = 'LED蛍光灯 ビームテック'
data2rakuten = 'さくらんぼ 大國屋'
data3 = 'さくらんぼ贈答用'
data4 = 'メロン贈答用'
r = 1
r2 = 1
y = 1
y2 = 1
y3 = 1
y4 = 1
i = 0

# @timeout(60)
# def check1():
#     sleep(10)
#     x,y = pyautogui.locateCenterOnScreen('rakuten.png',grayscale=True)
#     print(x,y)

# @timeout(60)
# def check2():
#     sleep(10)
#     x,y = pyautogui.locateCenterOnScreen('tor.png',grayscale=True)
#     print(x,y)

# def rakuten():
#     global r
#     global i
#     i = 0
#     try:
#             check2()
#     except:
#             return False
#     while i < 3:
#         pyperclip.copy('https://search.rakuten.co.jp/search/mall/%E3%81%84%E3%81%A1%E3%81%94+%E3%82%AE%E3%83%95%E3%83%88+%E5%A4%A7%E5%9C%8B%E5%B1%8B/?f=1&grp=product')
#         pyautogui.moveTo(450,96,0.5)
#         pyautogui.click(450.96)
#         pyautogui.hotkey('command', 'v')
#         sleep(10)
#         pyautogui.press('enter')
#         try:
#                 check1()
#                 print('rakuten %s' % r)
#                 pyautogui.moveTo(1021,96,0.5)
#                 pyautogui.click(1021,96)
#                 sleep(30)
#                 pyautogui.moveTo(850,170,0.5)
#                 pyautogui.click(850,170)
#                 sleep(30)
#                 r += 1
#                 # i = 3
#                 break
#         except:
#                 print('error')
#                 pyautogui.moveTo(1021,96,0.5)
#                 pyautogui.click(1021,96)
#                 sleep(30)
#                 pyautogui.moveTo(850,170,0.5)
#                 pyautogui.click(850,170)
#                 sleep(30)
#                 i += 1

def yahoo():
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
        elem.send_keys(data1, Keys.RETURN)
        sleep(30)

        print('yahoo %s' % y)
        sleep(30)
        browser.close()
        browser.quit()
        y += 1
    except:
        sleep(90)
        print('yahoo error')
        browser.close()
        browser.quit()

def yahooLED():
    global y2
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
        elem.send_keys(data2, Keys.RETURN)
        sleep(30)

        print('yahooLED %s' % y2)
        sleep(30)
        browser.close()
        browser.quit()
        y2 += 1
    except:
        sleep(90)
        print('yahoo error')
        browser.close()
        browser.quit()

def yahoo3():
    global y3
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
        elem.send_keys(data3, Keys.RETURN)
        sleep(30)

        print('yahooTop %s' % y3)
        sleep(30)
        browser.close()
        browser.quit()
        y3 += 1
    except:
        sleep(90)
        print('yahoo error')
        browser.close()
        browser.quit()

def yahoo4():
    global y4
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
        elem.send_keys(data4, Keys.RETURN)
        sleep(30)

        print('yahooTop %s' % y4)
        sleep(30)
        browser.close()
        browser.quit()
        y4 += 1
    except:
        sleep(90)
        print('yahoo error')
        browser.close()
        browser.quit()

def rakuten():
    global r
    # print("error rakuten")
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('network.proxy.type', 1)
    firefox_profile.set_preference('network.proxy.socks', '127.0.0.1')
    firefox_profile.set_preference('network.proxy.socks_port', 9150)
    
    browser = webdriver.Firefox(firefox_profile=firefox_profile)

    browser.get("https://search.rakuten.co.jp/search/mall")
    sleep(60)

    wait = WebDriverWait(browser, 120) # 最大120秒
    try:
        elem = wait.until( expected_conditions.element_to_be_clickable( (By.ID,"ri-cmn-hdr-sitem")) )
        elem = browser.find_element_by_id("ri-cmn-hdr-sitem")
        sleep(30)
        elem.send_keys(data1rakuten, Keys.RETURN)
        sleep(30)
        print('rakuten %s' % r)
        r += 1
        sleep(30)
        browser.close()
        browser.quit()
    except:
        print("error!!rakuten")
        sleep(90)
        browser.close()
        browser.quit()

def rakuten2():
    global r2
    # print("error rakuten")
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('network.proxy.type', 1)
    firefox_profile.set_preference('network.proxy.socks', '127.0.0.1')
    firefox_profile.set_preference('network.proxy.socks_port', 9150)
    
    browser = webdriver.Firefox(firefox_profile=firefox_profile)

    browser.get("https://search.rakuten.co.jp/search/mall")
    sleep(60)

    wait = WebDriverWait(browser, 120) # 最大120秒
    try:
        elem = wait.until( expected_conditions.element_to_be_clickable( (By.ID,"ri-cmn-hdr-sitem")) )
        elem = browser.find_element_by_id("ri-cmn-hdr-sitem")
        sleep(30)
        elem.send_keys(data2rakuten, Keys.RETURN)
        sleep(30)
        print('rakuten %s' % r2)
        r2 += 1
        sleep(30)
        browser.close()
        browser.quit()
    except:
        print("error!!rakuten")
        sleep(90)
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
    try:
        # pyautogui.screenshot('%s.png' % datetime.now())
        browser.close()
        browser.quit()
    except:
        print('error')
        browser.close()
        browser.quit()

def main():
    global i
    #  len(l) or (r <= len(l) and y <= len(l))
    while True:
        # ipアドレスチェック
        check33()
        # yahoo()
        # sleep(210)
        # sleep(150)

        yahoo()

        sleep(5)

        # rakuten()
        sleep(150)

        sleep(5)

        yahooLED()

        # rakuten2()
        sleep(150)

        sleep(randint(10,20))

if __name__ == "__main__":
    while True:
        main()
