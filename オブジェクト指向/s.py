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
data1 = 'いちご ギフト 大國屋'
data2 = 'LED 蛍光灯 ビームテック'
r = 1
y = 1
y2 = 1
i = 0

@timeout(60)
def check1():
    sleep(10)
    x,y = pyautogui.locateCenterOnScreen('rakuten.png',grayscale=True)
    print(x,y)

@timeout(60)
def check2():
    sleep(10)
    x,y = pyautogui.locateCenterOnScreen('tor.png',grayscale=True)
    print(x,y)

def rakuten():
    global r
    global i
    i = 0
    try:
            check2()
    except:
            return False
    while i < 3:
        pyperclip.copy('https://search.rakuten.co.jp/search/mall/%E3%81%84%E3%81%A1%E3%81%94+%E3%82%AE%E3%83%95%E3%83%88+%E5%A4%A7%E5%9C%8B%E5%B1%8B/?f=1&grp=product')
        pyautogui.moveTo(470,75,0.5)
        pyautogui.click(470.75)
        pyautogui.hotkey('command', 'v')
        sleep(10)
        pyautogui.press('enter')
        try:
                check1()
                print('rakuten %s' % r)
                pyautogui.moveTo(985,75,0.5)
                pyautogui.click(985,75)
                sleep(30)
                pyautogui.moveTo(838,149,0.5)
                pyautogui.click(838,149)
                sleep(30)
                r += 1
                # i = 3
                break
        except:
                print('error')
                pyautogui.moveTo(985,75,0.5)
                pyautogui.click(985,75)
                sleep(30)
                pyautogui.moveTo(838,149,0.5)
                pyautogui.click(838,149)
                sleep(30)
                i += 1

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
        pyautogui.screenshot('%s.png' % datetime.now())

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
        pyautogui.screenshot('%s.png' % datetime.now())

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

def check33():
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('network.proxy.type', 1)
    firefox_profile.set_preference('network.proxy.socks', '127.0.0.1')
    firefox_profile.set_preference('network.proxy.socks_port', 9150)

    browser = webdriver.Firefox(firefox_profile=firefox_profile)

    # ipアドレスチェック
    browser.get("https://www.cman.jp/network/support/go_access.cgi")
    try:
        pyautogui.screenshot('%s.png' % datetime.now())
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
        # sleep(100)
        # rakuten
        # now = datetime.now()
        # print(now)

        

        # pyautogui.moveTo(330,77,0.5)
        # pyautogui.click(330,77)

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
        # rakuten
        # sleep(60)
        # # if(r < 100):
        # #         rakuten(i)
        # sleep(60)
        # yahoo
        yahoo()
        rakuten()
        i = 4 - i
        sleep(60 * i)
        yahooLED()

if __name__ == "__main__":
        main()
