from hashlib import md5
import json
from urllib import parse
import time
import random
import requests
from pandas import json_normalize

def generate_sign(params):
    keys = sorted([key for key in params])
    p = ''.join([key + params[key] for key in keys])
    i = "6C57AB91A1308E26B797F4CD382AC79D"
    v = params["method"] + p + i

    sign = md5(v.encode())
    return sign.hexdigest().upper()


def url2params_and_sign(origin_url):
    url = parse.unquote(parse.unquote(origin_url))
    # print(url)
    lst = url.split('?')
    base_url = lst[0]
    param_str = lst[1]
    param_lst = param_str.split('&')
    params = {}
    for param in param_lst:
        ps = param.split('=')
        if ps[0] == 'callback':
            continue
        if ps[0] == 'sign':
            origin_sign = ps[1]
            continue
        params[ps[0]] = str(ps[1])
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    params['t'] = t
    return base_url, params, origin_sign


def param2url(base_url, params, sign):
    params['sign'] = sign
    url = base_url + '?' + parse.urlencode(params)
    del params['sign']
    return url


def main():
    url = 'https://api.ddky.com/cms/rest.htm?method=ddky.cms.search.cate.list.recipe.bianli&orderTypeId=0&city=%E5%8C%97%E4%BA%AC%E5%B8%82&lat=39.91511237702834&lng=116.40395508249037&shopId=100012&suite=1&pageNo=5&pageSize=20&wd=&unique=C3D88EC303F680A523EA591C0E9D3DD1&versionName=5.4.2&compositeId=45&plat=H5&platform=H5&t=2020-8-18%2016%3A37%3A13&v=1.0&sign=1605170445DCBF6C80CF532A15812D3C&callback=jsonp5'
    base_url, params, origin_sign = url2params_and_sign(url)
    # print(sorted([key for key in params]))
    pro_data = []
    for i in range(1, 20):
        params['pageNo'] = str(i)
        sign = generate_sign(params)
        # print(origin_sign, ' ', sign)
        url = param2url(base_url, params, sign)
        print(url)
        response = requests.get(url)
        # print(response.text)
        data = json.loads(response.text)
        print(data["data"]["productList"])
        productList = data["data"]["productList"]
        pro_data += productList
        time.sleep(random.randint(1, 4))

    # print(pro_data)
    pro_data_list = []
    format_item = {}
    for item in pro_data:
        format_item = {
            "name": item["name"],
            "productPrice": item["productPrice"],
            "saleVolumeNew": item["saleVolumeNew"],
            "shopName": item["shopName"],
            "productsArea": item["productsArea"],
            "productSpecifications": item["productSpecifications"],
            "imgUrl": item["imgUrl"],
        }
        pro_data_list.append(format_item)

    print(pro_data_list)
    df = json_normalize(pro_data_list)
    df.to_excel("product.xlsx")


if __name__ == '__main__':
    main()
