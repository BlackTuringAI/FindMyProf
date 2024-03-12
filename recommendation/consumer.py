import calculateRank_csv
import resultSorted
import re
from kafka import KafkaConsumer

consumer=KafkaConsumer("test",bootstrap_servers='localhost:9092')

for i in consumer:
    print(i)
    record=i.value.decode()
    ID=re.split(",",record)[0]
    degree=re.split(",",record)[1]
    n=re.split(",",record)[2]
    calculateRank_csv.main(ID,degree)#所有教授的ranking结果
    resultSorted.sort_csv_by_column(n)#评分最高的n名教授的ranking结果
