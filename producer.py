from kafka import KafkaProducer
from const import *

producer = KafkaProducer(bootstrap_servers=['172.31.91.151:9092'])
for i in range(100):
    msg = 'My ' + str(i) + 'st message'
    print ('Sending message: ' + msg)
    producer.send('my-first-topic', value=msg.encode())

producer.flush()
