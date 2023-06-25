from kafka import KafkaConsumer
from const import *
import sys

consumer = KafkaConsumer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT],
                         security_protocol='SASL_PLAINTEXT',
                         sasl_mechanism='PLAIN',
                         sasl_plain_username='fmc',
                         sasl_plain_password='fmc-pass')
try:
  topic = sys.argv[1]
except:
  print ('Usage: python3 consumer <topic_name>')
  exit(1)
  
consumer.subscribe([topic])
for msg in consumer:
    print (msg.value)
