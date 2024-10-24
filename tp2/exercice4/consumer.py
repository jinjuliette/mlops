from kafka import KafkaConsumer, KafkaProducer
import load_model as lm
import json

consumer = KafkaConsumer('jin', bootstrap_servers='51.38.185.58:9092', group_id='jin_prediction_group')

for msg in consumer:
    data = json.loads(msg.value)
    size = data['size']
    nb_rooms = data['nb_rooms']
    garden = data['garden']
    price = lm.predict([[size, nb_rooms, garden]])
    print("The price of the house will be: ", price[0], ".")

    producer = KafkaProducer(bootstrap_servers='51.38.185.58:9092')
    message = f"The price of the house will be: {price}.".encode('utf-8')
    producer.send('prediction_jin', value=message)
    producer.flush()