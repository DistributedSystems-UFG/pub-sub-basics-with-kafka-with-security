from kafka import KafkaProducer
from const import *
import sys

try:
    topic = sys.argv[1]
except:
    print ('Usage: python3 producer <topic_name>')
    exit(1)
    
producer = KafkaProducer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT],
                         security_protocol='SASL_PLAINTEXT',
                         sasl_mechanism='PLAIN',
                         sasl_plain_username='fmc',
                         sasl_plain_password='fmc-pass')
for i in range(100):
    msg = 'My ' + str(i) + 'st message for topic ' + topic
    print ('Sending message: ' + msg)
    producer.send(topic, value=msg.encode())

producer.flush()
