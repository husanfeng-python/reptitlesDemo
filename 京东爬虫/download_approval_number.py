# !/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import requests
import sys


def getapproval(url):
    # url = 'https://item.jkcsjd.com/19593163021.html#product-detail'

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}

    response = requests.get(url, headers=headers)
    matchObj = re.match(r'[\s\S]*批准文号</dt><dd>(.*)</dd>[\s\S]*',response.text)
    result = ''
    if matchObj:
        result = matchObj.group(1)
    return result
# print(response.text)