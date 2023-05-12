import time

import requests
from selenium import webdriver


def init_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')  # 禁用沙箱
    chrome_options.add_argument('--disable-dev-shm-usage')  # 禁用开发者shm
    driver = webdriver.Chrome('D:\\WorkSpace\\chromedriver.exe', options=chrome_options)

    return driver


def login(driver, url):
    driver.get(url)
    driver.find_element_by_id('username').send_keys('201921098210')
    driver.find_element_by_id('password').send_keys('hzy145235...')
    time.sleep(0.1)
    driver.find_element_by_id('login_submit').click()


def sleep(secs):
    time.sleep(secs)


def send_message(url, message):
    header = {
        "Content-Type": "application/json"
    }
    json = {
        "msgtype": "text",
        "text": {
            "content": message,
            "mentioned_list": ["@all"]
        }
    }
    # 通过params传参
    requests.post(url=url, json=json, headers=header)


driver = init_driver()
url = 'https://wfw.scuec.edu.cn/2021/08/29/book'
try:
    login(driver, url)
    while True:
        # 跳转至最新日期的预约页面
        dataLinks = driver.find_elements_by_css_selector('li.col-xs-4')
        dataLinks[-1].click()
        columns = driver.find_elements_by_css_selector('.reserveCol')
        submit = driver.find_element_by_css_selector('#submit')

        for i in range(1, len(columns)):
            elements = columns[i].find_elements_by_css_selector('li.canRes')
            for j in range(0, len(elements) - 2):
                columns[j].click()
                submit.click()

                time.sleep(0.2)

                place = elements[j].get_attribute('place')
                # print(place, j)

                resultElement = driver.find_element_by_css_selector('body > div.sweet-alert.showSweetAlert > h2')
                result = resultElement.text

                element = driver.find_element_by_css_selector('.confirm')
                element.click()

                if result == '锁定成功':
                    checkbox = driver.find_element_by_css_selector(
                        '#friendsTable > thead > tr > th.bs-checkbox > div.th-inner > label > input')
                    checkbox.click()
                    time.sleep(0.2)
                    final_submit = driver.find_element_by_css_selector('#end_submit > button')
                    final_submit.click()
                    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=44cf950c-0584-461c-9099-3ee80f3f8a5c'
                    send_message(url, place + ' ' + j)
                    break
finally:
    driver.quit()
