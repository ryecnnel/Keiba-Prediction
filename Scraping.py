import selenium
from selenium import webdriver

import time
import pandas as pd
import tool 

# GoogleChromeを起動
browser = webdriver.Chrome()
browser.implicitly_wait(3)


from bs4 import BeautifulSoup
# import urllib.request as req
# urllibはURLを操作する

YM = tool.ym()
ym_list = []
title_list = []

for ym in YM:
    url = "https://priconne-redive.jp/news/?ym=" + ym
    browser.get(url)

    #urlへ遷移する前に下の処理に行かないための記述
    time.sleep(3)

    parse_html = BeautifulSoup(browser.page_source, 'html.parser') 
    #クリックの動作を入力
    while  browser.find_elements_by_css_selector('div.btn_news_more a'):
        browser_from = browser.find_elements_by_css_selector('div.btn_news_more a')
        browser_from[0].click()
        time.sleep(3)
        parse_html = BeautifulSoup(browser.page_source, 'html.parser')

    title_lists = parse_html.find_all('h4')

    for i in title_lists:
        title_list.append(i.string)
        ym_list.append(ym)


df = pd.DataFrame({'YM': ym_list, 'Title':title_list})
df.to_csv('data/priconne.csv')
