from kafka import KafkaProducer
import pandas as pd
import json
import time

BOOTSTRAP_SERVERS = "localhost:9092"
TOPIC_NAME = "transactions"

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

df = pd.read_csv("fraudTest.csv")

print(f"Loaded {len(df)} transactions.\n")

for _, row in df.iterrows():

    message = row.to_dict()

    producer.send(TOPIC_NAME, message)
    producer.flush()

    print("=" * 60)
    print(f"Transaction ID : {message['trans_num']}")
    print(f"Amount         : ${message['amt']}")
    print(f"Merchant       : {message['merchant']}")
    print(f"Fraud Label    : {message['is_fraud']}")
    print("Status         : Sent to Kafka")
    print("=" * 60)

    time.sleep(1)

print("Streaming completed.")