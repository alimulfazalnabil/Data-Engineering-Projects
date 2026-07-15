import io

import avro.io
from avro import schema
from avro.io import DatumReader
from confluent_kafka import Consumer

TOPIC = 'sensor-readings'
schema_text = open('sensor.avsc', 'r', encoding='utf-8').read()
avro_schema = schema.parse(schema_text)
reader = DatumReader(avro_schema)

conf = {'bootstrap.servers': 'localhost:9092', 'group.id': 'mygroup', 'auto.offset.reset': 'earliest'}
consumer = Consumer(conf)
consumer.subscribe([TOPIC])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        continue
    bytes_reader = io.BytesIO(msg.value())
    decoder = avro.io.BinaryDecoder(bytes_reader)
    data = reader.read(decoder)
    print(f'Received: {data}')
