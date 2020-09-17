# !/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import time
from selenium import webdriver
import sys

mobile_emulation = {'deviceName': 'iPhone 6'}
options = webdriver.ChromeOptions()
# port=sys.argv[1]
# options.add_argument('--proxy-server=http://localhost:'+str(port))
options.add_experimental_option("mobileEmulation", mobile_emulation)
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(chrome_options=options)


# url = 'https://daojia.jd.com/html/index.html#goodsDetails/storeId:11645612/orgCode:74421/skuId:2002969218/spuId:undefined'


def find_tag(browser):
    lst = ['批准文号', '注册证号', '执行标准']
    els = browser.find_elements_by_tag_name('strong')
    approval_number = '无批准文号'
    for item in lst:
        if item in browser.page_source:
            for el in els:
                if el.text == item:
                    try:
                        pp = el.find_element_by_xpath('./..').find_element_by_xpath('./..')
                        ppp = pp.find_element_by_xpath('./..')
                        pppc = ppp.find_elements_by_xpath('./*')
                        approval_number_container = None
                        l = len(pppc)
                        for i in range(l):
                            if pppc[i] == pp:
                                approval_number_container = pppc[i + 1]
                                approval_number = approval_number_container.text
                                break
                    finally:
                        pass
                    break
            break
    return approval_number


def get_approval_number(url):
    browser.get(url)
    browser.refresh()
    time.sleep(2)

    approval_number = find_tag(browser)
    return approval_number


# lst = []

s = set()
with open('./daojiadata/items.txt', 'r', encoding='utf-8') as f:
    for line1 in f:
        data = json.loads(line1)
        if not s.__contains__(data['skuId']):
            s.add(data['skuId'])
            url = 'https://daojia.jd.com/html/index.html#goodsDetails/storeId:{}/orgCode:{}/skuId:{}/spuId:undefined'.format(
                data['storeId'], data['orgCode'], data['skuId'])
        # lst.append(url)
        approval_number = get_approval_number(url)
        print(data['skuId'], approval_number, url)
        with open('./daojiadata/approval_number.txt', 'a', encoding='utf-8') as file:
            file.write(','.join([data['skuId'], approval_number, url, '\n']))
browser.refresh()

print(len(s))
