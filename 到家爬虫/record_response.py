import json
from urllib.parse import urlparse, unquote, parse_qs
import re
import os


def extract_approval_number(html):
    if '批准文号' in html:
        matchObj = re.match(r'[\s\S]*批准文号[\s\S]*?<span[\s\S]*?">(.*?)></span[\s\S]*', html)
    elif '注册证号' in html:
        matchObj = re.match(r'[\s\S]*注册证号[\s\S]*?<span[\s\S]*?">(.*?)</span[\s\S]*', html)
    else:
        return '匹配不成功'
    if matchObj:
        return matchObj.group(1)
    return '匹配不成功'


def request(flow):
    pass


def response(flow):
    if 'client' in flow.request.url:
        # print(flow.response.text)
        url = unquote(unquote(flow.request.url))
        # print(url)

        result = urlparse(url)
        query_dict = parse_qs(result.query)

        # print(query_dict)
        data = json.loads(flow.response.text)
        if data['code'] == '0':
            result2 = data['result']
            method = query_dict['functionId'][0]
            if method == 'store/storeDetailV220':
                # 获取的是品类数据
                cateList = result2['cateList']
                for cate in cateList:
                    if not os.path.exists('./daojiadata'):
                        os.mkdir('./daojiadata')
                    with open('daojiadata/cateList.txt', 'a', encoding='utf-8') as file:
                        file.write(json.dumps(cate, ensure_ascii=False))
                        file.write('\n')
            elif method == 'storeIndexSearch/searchByCategoryPost':
                if len(result2['searchCatResultVOList']) > 1:
                    if not os.path.exists('./daojiadata'):
                        os.mkdir('./daojiadata')
                    with open('./daojiadata/exception.txt', 'a', encoding='utf-8') as file:
                        file.write(flow.request.url)
                        file.write('\n')
                searchResultVOList = result2['searchCatResultVOList'][0]['searchResultVOList']
                for item in searchResultVOList:
                    if not os.path.exists('./daojiadata'):
                        os.mkdir('./daojiadata')
                    with open('./daojiadata/items.txt', 'a', encoding='utf-8') as file:
                        file.write(json.dumps(item, ensure_ascii=False))
                        file.write('\n')
                # print(searchResultVOList)
            elif method == 'product/detailV6_0':
                html = ''

                if not os.path.exists('./daojiadata'):
                    os.mkdir('./daojiadata')
                if 'detailInfo' in result2 and 'h5HtmlText' in result2['detailInfo']:
                    html = result2['detailInfo']['h5HtmlText']

                    approval_number = extract_approval_number(html)
                    if '匹配不成功' == approval_number:
                        with open('./daojiadata/approval_number.txt', 'a', encoding='utf-8') as file:
                            file.write(flow.request.url)
                            file.write('\n')
                            file.write('\n')
                            file.write(html)
                            file.write('\n')
                            file.write('\n')
                            file.write(approval_number)
                            file.write('\n')
                            file.write('\n')
                            file.write('\n')
                else:
                    with open('./daojiadata/approval_number.txt', 'a', encoding='utf-8') as file:
                        file.write('无html')
                        file.write('\n')
                        file.write('\n')
                        file.write('\n')
