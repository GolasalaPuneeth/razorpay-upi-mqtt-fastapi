import paho.mqtt.publish as publish

class MQTTTool:
    def __init__(self, broker_url: str, broker_port: int):
        self.broker_url = broker_url
        self.broker_port = broker_port

    def publish_message(self, topic: str, message: str):
        try:
            publish.single(topic, message, retain=False, hostname=self.broker_url, port=self.broker_port)
            print(f"Message published to topic '{topic}': {message}")
        except Exception as e:
            print(f"Failed to publish message: {e}")
