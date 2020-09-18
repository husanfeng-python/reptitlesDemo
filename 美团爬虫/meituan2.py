# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import sys

if __name__ == '__main__':
    from selenium import webdriver

    # mobile_emulation = {'deviceName': 'iPhone 6'}
    options = webdriver.ChromeOptions()
    # port = sys.argv[1]
    options.add_argument('--proxy-server=http://localhost:8887')
    options.add_experimental_option("mobileEmulation",  {'deviceName': 'iPhone 6'})
    options.add_argument("--test-type")
    options.add_argument("--ignore-certificate-errors")
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)

    js1 = '''
               Object.defineProperties(navigator,{
                 webdriver:{
                   get: () => false
                 }
               })
            '''

    js2 = '''
            alert (
                window.navigator.webdriver
            )
        '''

    js3 = '''
            window.navigator.chrome = {
                runtime: {},
                // etc.
             };
        '''

    js4 = '''
        Object.defineProperty(navigator, 'languages', {
          get: () => ['en-US', 'en']
        });
            '''

    js5 = '''
                Object.defineProperty(navigator, 'plugins', {
                    get: () => [1, 2, 3, 4, 5,6],
                });
            '''
    # browser.execute_script(js1)
    # browser.execute_script(js2)
    # time.sleep(2)
    # browser.execute_script(js3)
    # browser.execute_script(js4)
    # browser.execute_script(js5)
    # time.sleep(2)
    browser.get(
        "https://h5.waimai.meituan.com/waimai/mindex/menu?mtShopId=994234603189853&initialLat=39894302&initialLng=116369125&actualLat=39.967878&actualLng=116.453603")
    time.sleep(random.randint(16, 20))
    browser.execute_script(js1)
    browser.execute_script(js3)
    browser.execute_script(js4)
    browser.execute_script(js5)
    print('开始输入验证码----')
    name_input = browser.find_element_by_id('phoneNumInput')  # 找到用户名的框框
    pass_input = browser.find_element_by_id('codeInput')  # 找到输入验证码的框框
    verification_Code_button = browser.find_element_by_id('sendCodeBtnText')  # 找到发送验证码按钮
    login_button = browser.find_element_by_id('iloginBtn')  # 找到登录按钮

    name_input.clear()
    account = input("请输入手机号 >>>")
    name_input.send_keys(account)  # 填写手机号
    time.sleep(random.randint(5, 10))
    verification_Code_button.click()  # 点击验证码按钮
    pwd = input("请输入验证码>>>")
    pass_input.send_keys(pwd)  # 填写验证码

    time.sleep(random.randint(5, 10))
    login_button.click()  # 点击登录

    # browser.execute_script(js1)
    # browser.execute_script(js3)
    # browser.execute_script(js4)
    # browser.execute_script(js5)

    # time.sleep(5)
    # print('开始验证----')

    # yanzheng_button = browser.find_element_by_id('iLoginComp-tip-id')  # 找到验证按钮
    # yanzheng_button.click()
    #
    # time.sleep(10)
    # print('开始输入验证信息----')
    #
    # yanzheng_input = browser.find_element_by_id('yodaBirthdayCodeInput')  # 找到
    # sfz = input("请输入身份证后8位>>>")
    # yanzheng_input.send_keys(sfz)
    #
    # time.sleep(5)
    #
    # confirm_button = browser.find_element_by_id('yodaVerifyBtn')  # 找到确定
    # confirm_button.click()

    time.sleep(random.randint(15, 20))
    try:
        li = browser.find_element_by_xpath("//div[@class='_2sy9--Z1fMPns-oU5TeHVU']")
        ul = li.find_elements_by_xpath('./*')
    except:
        pass

    # for index, el in ul:
    for index, el in enumerate(ul):
        print('index分类个数===>', index)
        try:
            time.sleep(random.randint(5, 60))
            if index == 0:
                ul[3].click()
            if index == 1:
                ul[1].click()
            if index == 2:
                ul[5].click()
            if index == 3:
                ul[8].click()
            if index == 4:
                ul[4].click()
            if index == 5:
                ul[9].click()
            if index == 6:
                ul[7].click()
            if index == 7:
                ul[10].click()
            if index == 8:
                ul[2].click()
            if index == 9:
                ul[13].click()
            if index == 10:
                ul[16].click()
            if index == 11:
                ul[11].click()
            if index == 12:
                ul[14].click()
            if index == 13:
                ul[15].click()
            if index == 14:
                ul[6].click()
            if index == 15:
                ul[12].click()
            if index == 16:
                ul[19].click()
            if index == 17:
                ul[17].click()
            if index == 18:
                ul[20].click()
            if index == 19:
                ul[18].click()
            if index == 20:
                ul[22].click()
            if index == 21:
                ul[20].click()
            if index == 22:
                ul[24].click()
            if index == 23:
                ul[21].click()
            if index == 24:
                ul[23].click()

        except:
            pass



