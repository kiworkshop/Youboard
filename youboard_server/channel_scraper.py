# wizdeo에서 유투브 채널 순위를 300개(변경될 수 있음) scrap
# (추후 운영자가 youtuber 100명을 추려낼 수 있도록 더 많은 데이터를 scrap함)
import requests
import pathlib
import time
from selenium import webdriver
from datetime import datetime


URL_BASE = 'https://analytics.wizdeo.com/en/channels/search?country[in][0]=kr&search=&sort=score'
URL_ARGS = '&direction=desc&colgroups=classification,statistics,score&limit=50&evolution=_1w'
NEXT_PATHS = ['//*[@id="content-main"]/div[1]/div[2]/div[3]/div[6]/ul/li[3]/a',
    '//*[@id="content-main"]/div[1]/div[2]/div[3]/div[6]/ul/li[5]/a',
    '//*[@id="content-main"]/div[1]/div[2]/div[3]/div[6]/ul/li[6]/a',
    '//*[@id="content-main"]/div[1]/div[2]/div[3]/div[6]/ul/li[7]/a',
    '//*[@id="content-main"]/div[1]/div[2]/div[3]/div[6]/ul/li[7]/a'
    ]

def get_login_info():
    with open("wiz.txt", "r") as f:
        user_email = f.readline().strip('\n')
        user_pw = f.readline().strip('\n')
        return user_email, user_pw

def initialize_scraper(driver, url):
    driver.get(url)

def login(driver, user_email, user_pw):
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/ul/li[2]/a').click()
    email = driver.find_element_by_id('UserEmail')
    email.send_keys(user_email)
    pw = driver.find_element_by_id('UserPassword')
    pw.send_keys(user_pw)
    driver.find_element_by_xpath('//*[@id="UserLoginForm"]/div[4]/button').click()

def html_to_object(driver, n):
    common_xpath = '//*[@id="content-main"]/div[1]/div[2]/div[3]/div[4]/div/table/tbody/tr[' + str(n) + ']'
    rank = driver.find_element_by_xpath(common_xpath + '/td[2]').text[:-2]
    name = driver.find_element_by_xpath(common_xpath + '/td[3]').text
    category = driver.find_element_by_xpath(common_xpath + '/td[4]').text
    country = driver.find_element_by_xpath(common_xpath + '/td[8]').text
    subscribers = driver.find_element_by_xpath(common_xpath + '/td[12]').text.split('+')[0]
    url = driver.find_element_by_xpath(common_xpath + '/td[3]/div/div[3]/a').get_attribute("href")
    channel = {
        'rank': rank,
        'name': name,
        'category':category,
        'country':country,
        'subscribers':subscribers,
        'url':url
    }
    return channel

def turn_page(driver, page):
    element = driver.find_element_by_xpath(NEXT_PATHS[page])
    element.location_once_scrolled_into_view
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

def channel_scrap():
    driver = webdriver.Chrome('.\\chromedriver.exe')
    user_email, user_pw = get_login_info()
    url = URL_BASE + URL_ARGS
    initialize_scraper(driver, url)
    login(driver, user_email, user_pw)
    channels = []
    # 페이지당 50개 x 6페이지
    for page in range(6):
        for n in range(1, 51):
            channels.append(html_to_object(driver, n))
        if page == 5:
            break
        turn_page(driver, page)
    return channels