import requests

url = "https://u.geekbang.org/serv/v1/myclass/article   "

# payload = "{\"id\":5000}"
payload = {"class_id": 17, "article_id": 287756}
headers = {
    'Content-Type': "application/json",
    'Origin': "https://time.geekbang.org",
    'Accept-Encoding': "br, gzip, deflate",
    'Cookie': "_ga=GA1.2.730392940.1590498864; LF_ID=1590498863814-3758779-4266524; gksskpitn=5a728b31-f86f-4ad3-a03c-a8dac4b2bfdf; MEIQIA_TRACK_ID=1ZA9zxOD2RxvQaV4mriWNrtUfH7; p_h5_u=531BEE2D-6B9B-4F6F-A19B-DA55429549F9; selectedStreamLevel=LD; orderInfo={%22tips%22:%22%E6%88%91%E4%BB%AC%E5%B7%B2%E7%BB%8F%E4%B8%BA%E6%82%A8%E9%94%81%E5%AE%9A%E4%BA%86%E6%9C%AC%E6%9C%9F%E5%B8%AD%E4%BD%8D%EF%BC%8C%E8%AF%B7%E5%B0%BD%E5%BF%AB%E5%AE%8C%E6%88%90%E6%94%AF%E4%BB%98%EF%BC%8C%E8%8E%B7%E5%BE%97%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%A0%BC%22%2C%22list%22:[{%22count%22:1%2C%22image%22:%22https://static001.geekbang.org/resource/image/02/17/02005584a58e12007671450249097817.png%22%2C%22name%22:%22winter%20%E6%89%8B%E6%8A%8A%E6%89%8B%E5%B8%A6%E4%BD%A0%E5%AE%9E%E7%8E%B0%20ToyReact%20%E6%A1%86%E6%9E%B6%22%2C%22sku%22:100055401%2C%22price%22:{%22sale%22:980}}]%2C%22invoice%22:false%2C%22app_id%22:3%2C%22type%22:%22collegeTraning%22%2C%22customShare%22:%22%22%2C%22shareCode%22:%22%22%2C%22ignore%22:%22poster%22%2C%22cid%22:0%2C%22special%22:true%2C%22isFromTime%22:false%2C%22home_url%22:%22https://u.geekbang.org/%22%2C%22detail_url%22:%22https://u.geekbang.org/schedule%22%2C%22callbackUrl%22:%22https://u.geekbang.org/schedule?sku=100055401%22%2C%22hb%22:[]%2C%22utm_term%22:%22guanwang%22}; Hm_lvt_59c4ff31a9ee6263811b23eb921a5083=1597569348; GCID=51d163a-ded47c3-b1139b4-375368c; GRID=51d163a-ded47c3-b1139b4-375368c; Hm_lpvt_59c4ff31a9ee6263811b23eb921a5083=1599825488; _gid=GA1.2.1966154611.1601126082; gk_process_ev={%22count%22:1%2C%22utime%22:1601126083658%2C%22referrer%22:%22https://u.geekbang.org/lesson/17?article=224365&utm_source=pinpaizhuanqu&utm_medium=geektime&utm_term=guanwang&utm_campaign=guanwang&utm_content=0511%22%2C%22target%22:%22page_geektime_login%22}; GCESS=BQUEAAAAAAoEAAAAAAkBAQcEKg5kXwIExT5vXwEIV2EUAAAAAAADBMU.b18GBIVrlvcLAgUABAQALw0ADAEBCAED; Hm_lvt_317df4dd2b90de00d81de4a83235e0e8=1599875235,1599902729,1599905128,1601126086; Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6=1599875235,1599902729,1599905128,1601126086; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221335639%22%2C%22first_id%22%3A%22173174f88f8459-07a6fee548c493-396a4605-1049088-173174f88fa36%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22pinpaizhuanqu%22%2C%22%24latest_utm_medium%22%3A%22geektime%22%2C%22%24latest_utm_campaign%22%3A%22guanwang%22%2C%22%24latest_utm_content%22%3A%220511%22%2C%22%24latest_utm_term%22%3A%22guanwang%22%2C%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fu.geekbang.org%2Flesson%2F17%3Farticle%3D224365%26utm_source%3Dpinpaizhuanqu%26utm_medium%3Dgeektime%26utm_term%3Dguanwang%26utm_campaign%3Dguanwang%26utm_content%3D0511%22%7D%2C%22%24device_id%22%3A%22173174f88f8459-07a6fee548c493-396a4605-1049088-173174f88fa36%22%7D; acw_tc=2760777916011278835563972e4060f0739b8208fa3c9535fd40831f56baa4; MEIQIA_VISIT_ID=1i3EU3949BOGDp0FzeIhDkfd6OP; _gat=1; Hm_lpvt_317df4dd2b90de00d81de4a83235e0e8=1601128591; Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6=1601128591; SERVERID=3431a294a18c59fc8f5805662e2bd51e|1601128592|1601126081",
    'Connection': "keep-alive",
    'Accept': "application/json, text/plain, */*",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15",
    # 'Referer': "https://time.geekbang.org/course/detail/77-5000",
    'Referer': "https://u.geekbang.org/lesson/17?article=287756&utm_source=pinpaizhuanqu&utm_medium=geektime&utm_term=guanwang&utm_campaign=guanwang&utm_content=0511",
    'Content-Length': "11",
    'Accept-Language': "zh-cn",
    'Cache-Control': "no-cache",
    'Postman-Token': "****"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
