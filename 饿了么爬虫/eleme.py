#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import json_normalize
import json

productJson = []
productJson_form = []
with open("elemedata/elemeData.txt", 'r', encoding='utf-16') as f2:
    for line1 in f2:
        try:
            load_dict = json.loads(line1)
            # print(load_dict2)
            if load_dict["api"] == "mtop.venus.shopcategoryservice.getcategorydetail":
                for item in load_dict['data']['data'][0]["foods"]:
                    productJson.append(item)
        except:
            pass

for item in productJson:
    # print(item)
    try:
        obj = {
            '名称/规格': item['name'],
            '规格': item["drugInfo"]["药品规格"] if '药品规格' in item["drugInfo"] else '',
            '批准文号': item["drugInfo"]["批准文号"] if '批准文号' in item["drugInfo"] else '',
            '月售': item['sellText'],
            '评分': item['rateText'],
            'currentPrice': item['currentPrice'],
            'originalPrice': item['originalPrice'],
            'eleSkuId': item['eleSkuId']
        }
        productJson_form.append(obj)
    except:
        pass


flagObj = {}
list_final = []
for child in productJson_form:
    if child not in list_final:
        list_final.append(child)

print(list_final)
df = json_normalize(list_final)
df.to_csv("./elemedata/eleme20200922.csv")
