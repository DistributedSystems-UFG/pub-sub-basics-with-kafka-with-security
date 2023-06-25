# Very simple Kafka-based pub-sub example -- with simple authentication 

## Instructions to configure and run:

### For the Kafka broker:

#### Create a JAAS configuration file (name it something lik 'kafka_jaas.conf', and place it somewhere, such as in Kafka's config directory), with contents such as:

Note: This is basically the users database. Change the user names and passwords accordingly.

```
KafkaServer {
   org.apache.kafka.common.security.plain.PlainLoginModule required
   username="admin"
   password="admin-secret"
   user_admin="admin-secret"
   user_bot="bob-pass"
   user_alice="alice-pass";
};
```

#### Edit the server.properties configuration file to add the following lines (will use SASL with authentication using plaintext username and password -- not very secure, but illustrates the concept):

Note: Replace the IP address in the 5th line with that of the machine running the Kafka broker.

```
listeners=SASL_PLAINTEXT://0.0.0.0:9092
security.inter.broker.protocol=SASL_PLAINTEXT
sasl.mechanism.inter.broker.protocol=PLAIN
sasl.enabled.mechanisms=PLAIN
advertised.listeners=SASL_PLAINTEXT://100.24.104.41:9092
listener.security.protocol.map=SASL_PLAINTEXT:SASL_PLAINTEXT
```

#### Before starting Zookeeper, tell it where to find the JAAS configuration file:

```
$ cd <kafka_dir>
$ export KAFKA_OPTS="-Djava.security.auth.login.config=./config/kafka_jaas.conf"
$ ./bin/zookeeper-server-start.sh ./config/zookeeper.properties
```

#### Same thing before starting the Kafka server (in another shell on the same server machine):

``` 
$ cd <kafka_dir>
$ export KAFKA_OPTS="-Djava.security.auth.login.config=./config/kafka_jaas.conf"
$ ./bin/kafka-server-start.sh ./config/server.properties
```

#### Finally, check the code for the producer and consumer (`producer.py` and `consumer.py`) to make sure that the right user names and passwords are passed as keyword arguments when creating the KafkaProducer and KafkaConsumer, respectively. 
