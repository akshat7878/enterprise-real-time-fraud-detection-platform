from kafka import KafkaConsumer
import joblib
import json

from preprocessing import preprocess
from database import insert_prediction, close_connection

# Load model
model = joblib.load("models/fraud_model.pkl")
encoders = joblib.load("models/label_encoders.pkl")

# Kafka Consumer
consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    group_id="fraud-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Listening for transactions...")

try:
    for message in consumer:

        transaction = message.value

        processed_df = preprocess(transaction, encoders)

        prediction = model.predict(processed_df)[0]
        probability = model.predict_proba(processed_df)[0][1]

        insert_prediction(transaction, prediction, probability)

except KeyboardInterrupt:
    print("Stopping consumer...")

finally:
    close_connection()
    consumer.close()
