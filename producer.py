from kafka import KafkaProducer
from const import *
import sys

try:
    topic = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
except:
    print ('Usage: python3 producer <topic_name> <username> <password>')
    exit(1)
    
producer = KafkaProducer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT],
                         security_protocol='SASL_PLAINTEXT',
                         sasl_mechanism='PLAIN',
                         sasl_plain_username=username,
                         sasl_plain_password=password)
for i in range(100):
    msg = 'My ' + str(i) + 'st message for topic ' + topic
    print ('Sending message: ' + msg)
    producer.send(topic, value=msg.encode())

producer.flush()
