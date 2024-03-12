from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')   #连接kafka

id=input("What is your ID?")
#academicStatus=input("What is your academic status?")
#faculty=input("What is your faculty?")
program=input("What is your program?")
#major=input("What is your major?")
#interest=input("What is your research interest?")
n=input("How many recommendations do you need to show you? Please fill in the integer.")

msg=id+","+program+","+n
msg = msg.encode('utf-8')
producer.send('test', msg)

producer.close()