import config
import paho.mqtt.client as mqtt
import logging
import json
import data_manager


# Initialize logger
logger = logging.getLogger(__name__)

class WattageMqttClient:
    def __init__(self, data_manager_instance):
        self.mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
        self.topic = config.MQTT_TOPIC                      # config
        self.broker = config.MQTT_BROKER_ADDRESS            # config
        self.port = config.MQTT_BROKER_PORT                 # config
        self.keepalive = config.MQTT_KEEPALIVE              # from config
        self.data_manager = data_manager_instance           # Store the data_manager instance

        # Assign instance's methods as callbacks for the paho-mqtt client
        self.mqtt_client.on_connect = self._on_connect      # Using internal names 
        self.mqtt_client.on_message = self._on_message      # Using internal names 


    def _on_connect(self, client, userdata, flags, rc):

        if rc == 0:
            logger.info(f"Connected to MQTT broker at {self.broker}:{self.port} with reason code {rc}")
            client.subscribe(self.topic)
            logger.info(f"Subscribed to topic: {self.topic}")
        else:
            logger.warning(f"Failed to connect to MQTT broker with reason code {rc}")


    def _on_message(self, client, userdata, msg):
        logger.info(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

        try:
            payload = json.loads(msg.payload.decode())
            reader_data = payload.get("reader_data", [])
            time_value = reader_data["metadata"]["time"]
            for item in reader_data:
                if "1-0:1.7.0.255" in item:
                    watt_value = float(item["1-0:1.7.0.255"])
                    watt_value = watt_value * 1000                 
                    break

            if watt_value is not None:
                self.data_manager.set_latest_raw_wattage(watt_value, time_value) # Pass the values to data manager
                logger.info(f"Latest wattage value: {watt_value} W at {time_value}")

            else:
                logger.warning(f"Wattage not found in MQTT payload: {payload}")

        except Exception as e:
            logger.error(f"[MQTT] Failed to parse message: {e}")

    


    def start(self):

        try:
            self.mqtt_client.connect(self.broker, self.port, keepalive=60)
            logger.info(f"Connecting to MQTT broker at {self.broker}:{self.port}")
            self.mqtt_client.loop_start()
            logger.info("MQTT client network loop started")
        except Exception as e:
            logger.critical(f"[MQTT] Connection failed: {e}")




    def stop(self):
        self.mqtt_client.loop_stop()
        self.mqtt_client.disconnect()
        logger.info("Disconnected from MQTT broker")