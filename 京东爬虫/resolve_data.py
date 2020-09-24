import re
from lxml import etree
import json
import requests
from pandas import json_normalize
import pandas as pd
import random, time


def getapproval2(uid):
    pass

def getapproval(url):
    print(url)
    # url = 'https://item.jkcsjd.com/19593163021.html#product-detail'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}

    response = requests.get(url, headers=headers)
    matchObj = re.match(r'[\s\S]*批准文号</dt><dd>(.*)</dd>[\s\S]*', response.text)
    result = ''
    if matchObj:
        result = matchObj.group(1)
    time.sleep(random.randint(1,3))
    return result

# resolve data
dic = {}
with open('./data/mgets.txt', 'r', encoding='utf-8') as f:
    for line1 in f:
        try:
            if line1 != None and line1.strip() != '':
                content = line1.split('(')[1][:-3]
                data = json.loads(content)
                for item in data:
                    id = item['id'].replace('J_','')
                    dic[id] = {
                        'p': item['p'],
                        'm': item['m']
                    }
        except Exception as e:
            print(e)


lst = []
with open('./data/getModuleHtml.txt', 'r', encoding='utf-8') as f:
    for line1 in f:
        try:
            # print(line1)
            data = json.loads(line1.replace('jshop_module_render_callback(','')[:-2])
            # print(data)
            html = etree.HTML(data['moduleText'])
            jGoodsInfos = html.xpath('//div[@class="jGoodsInfo"]')
            for jGoodsInfo in jGoodsInfos:
                try:
                    aa = jGoodsInfo.xpath('./div[@class="jDesc"]/a')
                    if aa != None and len(aa)> 0:
                        a = jGoodsInfo.xpath('./div[@class="jDesc"]/a')[0]
                        url = a.get('href')
                        pattern = r'//item.jd.com/(\d+).html'
                        a1 = re.match(pattern, url)
                        uid = a1.group(1)
                        price = '0'
                        if dic.__contains__(uid):
                            price = dic[uid]['p']
                        name = a.text
                        eval_num = jGoodsInfo.xpath('./div[@class="extra"]/span/a')[0].text.replace('已有','').replace('人评价', '')
                        detail_url = 'https://item.jkcsjd.com/' +uid+ '.html#product-detail'
                        approval = getapproval(detail_url)
                        with open('data/approval.txt', 'a', encoding='utf-8') as file:
                            file.write(','.join([uid, approval,'\n']))
                        item = {
                            'uid':uid,
                            'price':price,
                            'approval':approval,
                            'name': name,
                            'eval_num': eval_num
                        }
                        rr = ','.join([uid, price, approval, name, eval_num,'\n'])
                        with open('data/result.txt', 'a', encoding='utf-8') as file:
                            file.write(rr)
                        lst.append(item)
                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)


        # results = html.xpath('//a[starts-with(@href, "//item.jd.com")]')
        # for result in results:
        #     url = result.get('href')
        #     pattern = r'//item.jd.com/(\d+).html'
        #     a = re.match(pattern, url)
        #     if a.group() and result.text and result.text.strip() != '' and result.text.strip() != '立刻购买':
        #         uid = a.group(1)
        #         print(url, uid , result.text)

        # print(results)

df = json_normalize(lst)
filename= 'result.xlsx'
df.to_excel(filename)