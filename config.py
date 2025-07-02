# config.py

import os 

# --- Application Configuration ---
APP_NAME = "TRMNL Wattage Plugin"
FLASK_PORT = int(os.getenv("FLASK_PORT", 5000)) # Default Flask port

# --- MQTT Configuration ---
# Note: The paho-mqtt client takes address and port separately,
# so the full URL "mqtt://powerbuddy.duckdns.org:1883" is not needed here.
# Just the hostname/IP.
MQTT_BROKER_ADDRESS = os.getenv("MQTT_BROKER_ADDRESS", "powerbuddy.duckdns.org")
MQTT_BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT", 1883))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "/eniwa/energy/device/7CDFA1562F64/status/evt")
MQTT_USERNAME = os.getenv("MQTT_USERNAME", None) # Optional, set to None if not required
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", None) # Optional, set to None if not required
MQTT_CLIENT_ID = os.getenv("MQTT_CLIENT_ID", "trmnl_wattage_client") # A more descriptive ID
MQTT_KEEPALIVE = int(os.getenv("MQTT_KEEPALIVE", 60)) # Keepalive interval in seconds

# --- Graphing Configuration ---
GRAPH_WIDTH_INCHES = 8.0
GRAPH_HEIGHT_INCHES = 4.8
GRAPH_DPI = 100
GRAPH_UPDATE_INTERVAL_MINUTES = 10
DATA_BUFFER_SIZE = 6

# --- Logging Configuration ---
LOG_FILE = "plugin.log"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()