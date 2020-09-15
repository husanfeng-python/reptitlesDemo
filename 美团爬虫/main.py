# -*- coding: utf-8 -*-

import time
import random
import asyncio
from exe_js import *
from pyppeteer import launch


class MeiTuan_Spider():
    def __init__(self):
        pass


    @classmethod
    async def create_browser(cls):
        self = MeiTuan_Spider()
        self.browser = await launch({
            'headless': False,
            'args': ['--no-sandbox'],
            'userDataDir': './temporary',
            # 'args': ['--proxy-server=127.0.0.1:8080', ]
        })
        return self

    def input_time_random(self):
        return random.randint(100, 151)


    async def login(self, mobilephone):
        page = await self.browser.newPage()
        login_url = 'https://h5.waimai.meituan.com/login'
        await page.goto(login_url)
        await asyncio.sleep(3)
        await page.type('#phoneNumInput', mobilephone, {'delay': self.input_time_random() - 50})
        #
        #
        # # phoneNumInput
        sendCodeBtn = await page.querySelector('#sendCodeBtn')
        await sendCodeBtn.click()
        print('请输入验证码')
        password = input()
        await page.type('#codeInput', password, {'delay': self.input_time_random() - 50})
        # # iloginBtn
        iloginBtn = await page.querySelector('#iloginBtn')
        await iloginBtn.click()
        #
        # pass

    async def to_shop(self, shop_url):

        page = await self.browser.newPage()
        # await page.setUserAgent(
        #     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')

        await page.goto(shop_url)
        await page.evaluate(js1)
        await page.evaluate(js3)
        await page.evaluate(js4)
        await page.evaluate(js5)


        await asyncio.sleep(2)
        # #  dd data-tag="spu"  如何查找 具有data-tag 属性，并且值等于spu的dd元素
        # elements = await page.xpath("//dd[@data-tag='spu']")
        # for element in elements:
        #     content = await page.evaluate('(element) => element.textContent', element)
        #     print(content)

        # js = """
        # """
        # await page.evaluate(js)

        li_list = await page.xpath('//*[@id="scrollArea"]/div[3]/div/div[1]/div[1]/div[1]/div')
        print(len(li_list))
        for li in li_list:
            try:
                await li.click()
                await asyncio.sleep(random.randint(3,7))
            except Exception as e:
                print(e)
        await asyncio.sleep(20000)





async def main():
    to_shop_url = 'https://h5.waimai.meituan.com/waimai/mindex/menu?mtShopId=913888649237477&initialLat=39.895006&initialLng=116.368518&actualLat=39.895006&actualLng=116.368518&source=searchresult'
    meiTuan_Spider = await MeiTuan_Spider.create_browser()
    # await meiTuan_Spider.login('13716208918')
    await meiTuan_Spider.to_shop(to_shop_url)

if __name__ == '__main__':

    loop = asyncio.get_event_loop()

    loop.run_until_complete(main())


