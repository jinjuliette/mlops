from kafka import KafkaConsumer
import json
import numpy as np

consumer = KafkaConsumer('jin', bootstrap_servers='51.38.185.58:9092')

for msg in consumer:
    data = json.loads(msg.value)
    data = np.array(data['data'])
    sum = np.sum(data)
    print("total", sum)
