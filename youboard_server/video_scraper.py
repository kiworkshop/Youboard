# wizdeo에서 유투브 인기영상 top 100을 스크래이핑.
import pathlib
import time
from selenium import webdriver
from datetime import datetime


URL_BASE = 'https://analytics.wizdeo.com/en/videos/search?country%5Bin%5D%5B0%5D=kr'
URL_ARGS = '&limit=50&evolution=_1w&sort=NOVideo.views_1w&direction=desc'

NEXT_PATH = '//*[@id="content-main"]/div[1]/div[2]/div[5]/div[6]/ul/li[3]/a'

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
    common_xpath = '//*[@id="content-main"]/div[1]/div[2]/div[5]/div[4]/div/table/tbody/tr[' + str(n) + ']'
    rank = driver.find_element_by_xpath(common_xpath + '/td[2]').text[:-2]
    name = driver.find_element_by_xpath(common_xpath + '/td[3]').text
    channel = driver.find_element_by_xpath(common_xpath + '/td[4]').text
    category = driver.find_element_by_xpath(common_xpath + '/td[5]').text
    views = driver.find_element_by_xpath(common_xpath + '/td[8]/div/span').text
    lastWeekViews = driver.find_element_by_xpath(common_xpath + '/td[8]/div/div').text.split('+')[1]
    url = driver.find_element_by_xpath(common_xpath + '/td[3]/div/div[2]/div/a').get_attribute("href")
    video = {
        'rank': rank,
        'name': name,
        'channel': channel,
        'category': category,
        'views': views,
        'lastWeekViews': lastWeekViews,
        'url': url
    }
    print(video)
    return video

def turn_page(driver):
    element = driver.find_element_by_xpath(NEXT_PATH)
    element.location_once_scrolled_into_view
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

def video_scrap():
    driver = webdriver.Chrome('.\\chromedriver.exe')
    user_email, user_pw = get_login_info()
    url = URL_BASE + URL_ARGS
    initialize_scraper(driver, url)
    login(driver, user_email, user_pw)
    videos = []
    # 페이지당 50개 x 2페이지
    for page in range(2):
        for n in range(1, 51):
            videos.append(html_to_object(driver, n))
        if page == 1:
            break
        turn_page(driver)
    return videos

if __name__ == "__main__":
    video_scrap()