set -x
# 生成随机端口
function rand(){
    min=$1
    max=$(($2-$min+1))
    num=$(($RANDOM+1000000000)) #增加一个10位的数再求余
    echo $(($num%$max+$min))
}

port=$(rand 8080 8080)
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
rm -rf data/*
mkdir data
python main.py ${port}
python resolve_data.py


