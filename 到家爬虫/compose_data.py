import json
import pandas as pd
from pandas import json_normalize
import sys

# cate_path = './daojiadata/cateList.txt'
item_path = './daojiadata/items.txt'
approval_path = './daojiadata/approval_number.txt'
product_xlsx = './daojiadata/product.xlsx'
dic = dict()
with open(item_path, 'r', encoding='utf-8') as f:
    for line1 in f:
        data = json.loads(line1)

        item = {
            'skuId': data['skuId'],
            'skuName': data['skuName'],
            'imgUrl': data['imgUrl'],
            'storeId': data['storeId'],
            'funcIndicatinsOrAdWord': data['funcIndicatinsOrAdWord'],
            'basicPrice': data['skuPrice']['basicPrice'],
            'realTimePrice': data['skuPrice']['realTimePrice'],
            'vipPrice': data['vipPrice'],
            'monthSales': data['monthSales'],
            'highOpinion': data['highOpinion'],
            'stockCount': data['stockCount'],
            'standard': data['standard'] if 'standard' in data else '',
            'promotion': data['promotion'] if 'promotion' in data else ''
        }
        dic[data['skuId']] = item


with open(approval_path, 'r', encoding='utf-8') as f:
    lst = []
    for line1 in f:
        lst2 = line1.split(',')
        skuId = lst2[0]
        url = lst2[-1]
        approval_number = ' '.join(lst2[1:-2])
        if str(skuId) not in dic:
            dic[str(skuId)] = {}
        dic[str(skuId)]['url'] = url
        dic[str(skuId)]['approval_number'] = approval_number
        dic[str(skuId)]['skuId'] = skuId


lst = dic.values()

df = json_normalize(lst)
# filename=sys.argv[1]
df.to_excel(product_xlsx)