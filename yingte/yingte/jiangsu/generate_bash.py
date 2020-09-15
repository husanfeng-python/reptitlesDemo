import os, stat
import urllib.request
import pandas as pd

file_path = '润药商城OTC1.xlsx'
data = pd.read_excel(file_path, header=0)

data = data.dropna(subset=['商品主码'])
data[['PRODUCT_MDM_CODE']] = data[['商品主码']].astype(int)
data = pd.DataFrame(data, columns=['PRODUCT_MDM_CODE'])
prd_product_base_inf = 'prd_product_base_inf.csv'

data2 = pd.read_csv(prd_product_base_inf)

data3 = pd.merge(data, data2, how='inner', on='PRODUCT_MDM_CODE')
# print(data3.head())

data4 = pd.read_excel('jsonstr.xlsx')
print(data4.head())

def add_2(s):
    return str(s) + '_2'


data3['OBJ_KEY'] = data3['PRODUCT_BASE_INF_ID'].apply(add_2)

data3= data3.drop('PRODUCT_BASE_INF_ID', 1)
print(data3.head())
data5 = pd.merge(data3, data4, how='inner', on='OBJ_KEY')
#

import json
def get_image_list(s):
    if s.strip() == '':
        return ''
    data = json.loads(s)
    ll = []
    for item in data['imageValueEntryList']:
        try:
            ll.append(item['sysFileUrl'])
        except Exception as e:
            pass
    return ';'.join(ll)

data5['img_lst'] = data5['jsonstr'].apply(get_image_list)
data5= data5.drop('jsonstr', 1)
data5.to_csv('all.csv')



def download(img_url, file_path):
    file_name = img_url.split('/')[-1]
    try:
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        filename = '{}{}{}'.format(file_path, os.sep, file_name)
        urllib.request.urlretrieve(img_url, filename=filename)

    except IOError as e:
        pass
    except Exception as e:
        pass


csv_file = 'all.csv'
data = pd.read_csv(csv_file)
dic_map = set()
url_map = set()

for index, row in data.iterrows():
    img_lst = str(row['img_lst'])
    dir = str(row['PRODUCT_MDM_CODE'])
    if not dic_map.__contains__(dir):
        print('mkdir '+ dir )
        dic_map.add(dir)
    if img_lst != 'nan':
        imgs = img_lst.split(';')
        for img in imgs:
            if not img.startswith('http'):
                img = 'https://img.hrryzx.com/upload/'+'/'.join(img.split('/'))
            if not url_map.__contains__(img):
                print('wget '+img + ' -O ' + dir + '/'+ img.split('/')[-1])
                url_map.add(img)
