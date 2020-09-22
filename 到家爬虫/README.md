# 京东到家爬虫

## 安装必要的包
```
pip install mitmproxy
```

## 启动代理
```
mitmdump -s record_response.py -p 8880
```

## 运行py文件
```
python daojia_spider.py
```

## 数据整理
```
python compose_data.py
```