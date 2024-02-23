import calculateRank
import re
from kafka import KafkaConsumer

consumer=KafkaConsumer("test",bootstrap_servers='localhost:9092')

for i in consumer:
    print(i)
    record=i.value.decode()
    ID=re.split(",",record)[0]
    degree=re.split(",",record)[1]
    calculateRank.main(ID,degree)
