set -x
# 生成随机端口
function rand(){
    min=$1
    max=$(($2-$min+1))
    num=$(($RANDOM+1000000000)) #增加一个10位的数再求余
    echo $(($num%$max+$min))
}

port=$(rand 8000 10000)
echo $port
quit=0

while [ "$quit" -ne 1 ]; do
  netstat -a | grep $port >> /dev/null
  if [ $? -gt 0 ]; then
    quit=1
  else
    port=`expr $port + 1`
  fi
done

nohup mitmdump -s record_response.py -p ${port} &
sleep 3
rm -rf daojiadata/*
python daojia_spider.py ${port}
python download_approval_number.py

sdate=$(date +%Y%m%d)
storeId='11645612'
sname="京东到家"
sp='-'
filename=$sname$sp$storeId$sp$sdate'.xslx'
python compose_data.py filename
python send_wechat.py filename

