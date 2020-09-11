# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import sys


# print(sys.argv[0])          #sys.argv[0] 类似于shell中的$0,但不是脚本名称，而是脚本的路径


def scroll_to_bottom(driver):
    # js1 = 'document.getElementsByClassName("scroll-box")[0].scrollHeight = 10000'
    js = """
    lst = document.getElementsByClassName('scroll-wrap')
    if(lst.length > 0)
    {
        lst[0].scrollTo(0,10000)
    }
      """
    driver.execute_script(js)

    # scoll_item(driver)


if __name__ == '__main__':
    from selenium import webdriver

    mobile_emulation = {'deviceName': 'iPhone 6'}
    options = webdriver.ChromeOptions()
    # port = sys.argv[1]
    options.add_argument('--proxy-server=http://localhost:8888')
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument("--test-type")
    options.add_argument("--ignore-certificate-errors")
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(chrome_options=options)
    browser.get("https://daojia.jd.com/html/index.html#storeHome/storeId:11645612/orgCode:74421/needAddCart:0")
    # browser.implicitly_wait(4)
    time.sleep(6)
    btn_all_product = browser.find_element_by_xpath('//*[@id="tabbar"]/span[2]')
    btn_all_product.click()
    time.sleep(3)

    ul = browser.find_element_by_xpath('//ul[@class="store-goods-left "]')
    eles = ul.find_elements_by_xpath('./*')
    # eles = browser.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[2]/div[1]/ul')
    for el in eles:
        browser.execute_script("arguments[0].scrollIntoView();", el)
        time.sleep(1)
        el.click()
        time.sleep(random.randint(1, 3))
        childCategory = []
        try:
            childCategory = browser.find_element_by_class_name('childCategoryUl')
        except:
            pass
        if childCategory:
            childCategories = childCategory.find_elements_by_xpath('./*')
            for cc in childCategories:
                cc.click()
                time.sleep(random.randint(1, 3))
                scroll_to_bottom(browser)

        else:
            scroll_to_bottom(browser)
