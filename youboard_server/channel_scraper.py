# wizdeo에서 유투브 채널 순위 top 100을 scrap.
import requests
import pathlib
import time
from selenium import webdriver
from datetime import datetime


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

def channel_scrap():
    driver = webdriver.Chrome('.\\chromedriver.exe')
    user_email, user_pw = get_login_info()
    url_base = 'https://analytics.wizdeo.com/en/channels/search?country[in][0]=kr&search=&sort=score'
    url_args = '&direction=desc&colgroups=classification,statistics,score&limit=50&evolution=_1w'
    url = url_base + url_args
    initialize_scraper(driver, url)
    login(driver, user_email, user_pw)
    next_path = '//*[@id="content-main"]/div[1]/div[2]/div[3]/div[6]/ul/li[3]/a'
    channels = []
    # 페이지당 50개 x 2페이지
    for page in range(2):
        for n in range(1, 51):
            channels.append(html_to_object(driver, n))
        #페이지 넘김
        element = driver.find_element_by_xpath(next_path)
        element.location_once_scrolled_into_view
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    return channels