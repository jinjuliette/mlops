from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='51.38.185.58:9092')
for _ in range(2):
    producer.send('exo1', 'Bonjour, je m\'appelle Juliette Jin')
    producer.flush()