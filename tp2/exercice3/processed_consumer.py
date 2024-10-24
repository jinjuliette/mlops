from kafka import KafkaConsumer

consumer = KafkaConsumer('processed', bootstrap_servers='51.38.185.58:9092')
for msg in consumer:
    print (msg.value)