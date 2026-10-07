import paho.mqtt.publish as publish
from dotenv import load_dotenv
import os

load_dotenv()
class MQTTTool:
    def __init__(self):
        self.broker_url = os.getenv('MQTT_HOST')
        self.broker_port = int(os.getenv('MQTT_PORT'))

    def publish_message(self, topic: str, message: str):
        try:
            publish.single(topic, message, retain=False, hostname=self.broker_url, port=self.broker_port)
            print(f"Message published to topic '{topic}': {message}")
        except Exception as e:
            print(f"Failed to publish message: {e}")
