from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='51.38.185.58:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for _ in range(1):
    producer.send('jin', {'size': 100, 'nb_rooms': 3, 'garden': 1})
    producer.flush()