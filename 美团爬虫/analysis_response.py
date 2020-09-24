import json
from urllib.parse import urlparse, unquote, parse_qs
import re
import os


def request(flow):
    pass


def response(flow):
    if 'food' in flow.request.url:
        url1 = unquote(unquote(flow.request.url))
        print(url1)
        print('打印1------------------------------------')
        data = json.loads(flow.response.text)
        print('打印数据1=》', data['code'])
        if data['code'] == 0:
            categoryList = data['data']['categoryList']
            if len(categoryList) > 0:
                print('第一个分类数据=》', categoryList[0]['spuList'])
                for cate in categoryList[0].spuList:
                    if not os.path.exists('./meituandata'):
                        os.mkdir('./meituandata')
                    with open('meituandata/categoryList.txt', 'a', encoding='utf-8') as file:
                        file.write(json.dumps(cate, ensure_ascii=False))
                        file.write('\n')
            pageCategoryList = data['data']['pageCategoryList']
            if len(pageCategoryList) > 0:
                print('所有分类=》', pageCategoryList)

    if 'menuproducts' in flow.request.url:
        # print(flow.response.text)
        url = unquote(unquote(flow.request.url))
        print(url)
        print('打印2------------------------------------')
        data = json.loads(flow.response.text)
        print('打印数据2=》', data['code'])
        if data['code'] == 0:
            dataList = data['data']['spuList']
            # print('spuList=>', dataList)
            if len(dataList) > 0:
                for cate in dataList:
                    print('items==>', cate)
                    if not os.path.exists('./meituandata'):
                        os.mkdir('./meituandata')
                    with open('meituandata/productList.txt', 'a', encoding='utf-8') as file:
                        file.write(json.dumps(cate, ensure_ascii=False))
                        file.write('\n')
