from kafka import KafkaConsumer
from const import *
import sys

try:
  topic = sys.argv[1]
  username = sys.argv[2]
  password = sys.argv[3]
except:
  print ('Usage: python3 consumer <topic_name> <username> <password>')
  exit(1)

consumer = KafkaConsumer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT],
                         security_protocol='SASL_PLAINTEXT',
                         sasl_mechanism='PLAIN',
                         sasl_plain_username=username,
                         sasl_plain_password=password)
  
consumer.subscribe([topic])
for msg in consumer:
    print (msg.value)
