import asyncio
import datetime
import aiohttp
from pyppeteer import launch
from pyppeteer.network_manager import Request, Response
import random
import requests
# from exe_js import *
from 美团爬虫 import exe_js

from 美团爬虫.exe_js import js1, js3, js4, js5

last_proxy_time = datetime.datetime.now()
ip = None
aiohttp_session = aiohttp.ClientSession(loop=asyncio.get_event_loop())


def get_ip():
    global last_proxy_time
    global ip
    url = 'http://http.tiqu.alicdns.com/getip3?num=1&type=1&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4'

    now_time = datetime.datetime.now()
    durn = (now_time - last_proxy_time).seconds
    if ip == None or durn > 10:
        response = requests.get(url)
        ip = 'http://' + response.text.strip()
        print(ip)
        last_proxy_time = now_time
    return ip


async def intercept_request(req):
    await req.continue_()


async def intercept_request2(request: Request):
    """
        # 启用拦截器
        await page.setRequestInterception(True)
        page.on("request", use_proxy_base)
    :param request:
    :return:
    """
    # 构造请求并添加代理
    req = {
        "headers": request.headers,
        "data": request.postData,
        "proxy": get_ip(),  # 使用全局变量 则可随意切换
        "timeout": 5,
        "ssl": False,
    }
    try:
        # 使用第三方库获取响应
        async with aiohttp_session.request(
                method=request.method, url=request.url, **req
        ) as response:
            body = await response.read()
    except Exception as e:
        await request.abort()
        return

    # 数据返回给浏览器
    resp = {"body": body, "headers": response.headers, "status": response.status}
    await request.respond(resp)
    return


async def intercept_response(res):
    pass
    # if 'food' in res.request.url or 'menuproducts' in res.request.url :
    #     # 数据解析 入库
    #     # with open('data/meituan.txt', 'a', encoding='utf-8') as file:
    #     #     file.write(await res.text())
    #     #     file.write('\n')
    #     resp = await res.text()
    #     print(resp)


def input_time_random():
    return random.randint(100, 151)


async def main():
    browser = await launch({
        'headless': False,
        'devtools': True,
        'defaultViewport': {
            'width': 414,
            'height': 736,
            'deviceScaleFactor': 3,
            'isMobile': True,
            'hasTouch': True,
            'isLandscape': False
        },
    })
    [page] = await browser.pages()
    # page: Page = await browser.newPage()
    await page.setRequestInterception(True)
    page.on('request', intercept_request)
    page.on('response', intercept_response)
    shop_url = 'https://h5.waimai.meituan.com/waimai/mindex/menu?mtShopId=913888649237477&initialLat=39.895006&initialLng=116.368518&actualLat=39.895006&actualLng=116.368518&source=searchresult'

    await page.goto(shop_url)
    await page.evaluate(js1)
    await page.evaluate(js3)
    await page.evaluate(js4)
    await page.evaluate(js5)
    await asyncio.sleep(2)
    li_list = await page.xpath('//*[@id="scrollArea"]/div[3]/div/div[1]/div[1]/div[1]/div')
    print(len(li_list))
    for li in li_list:
        try:
            await li.click()
            await asyncio.sleep(random.randint(3, 7))
        except Exception as e:
            print(e)
    await asyncio.sleep(20000)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
