from kafka import KafkaConsumer, KafkaProducer

import json
import numpy as np


consumer = KafkaConsumer('jin', bootstrap_servers='51.38.185.58:9092')

for msg in consumer:
    data = json.loads(msg.value)
    data = np.array(data['data'])
    sum = np.sum(data)
    print("The total will be: ", sum, ".")

    producer = KafkaProducer(bootstrap_servers='51.38.185.58:9092')
    message = f"The total will be: {sum}.".encode('utf-8')
    producer.send('processed', value=message)
    producer.flush()
