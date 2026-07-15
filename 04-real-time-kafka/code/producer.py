import io
import random
import time

import avro.io
from avro import schema
from avro.io import DatumWriter
from confluent_kafka import Producer

TOPIC = 'sensor-readings'
schema_text = open('sensor.avsc', 'r', encoding='utf-8').read()
avro_schema = schema.parse(schema_text)
writer = DatumWriter(avro_schema)

conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(conf)

while True:
    data = {
        'sensor_id': random.randint(1, 10),
        'temperature': round(random.uniform(20, 30), 2),
        'timestamp': int(time.time()),
    }
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write(data, encoder)
    producer.produce(TOPIC, value=bytes_writer.getvalue())
    producer.flush()
    print(f'Sent: {data}')
    time.sleep(2)
