
To build a cloud-based IoT system using MQTT protocol and ThingSpeak, where a virtual environmental station periodically generates sensor values for:

Temperature
Humidity
CO2 Levels

📁 Project Structure
File	Description
sensor.py	Simulates a virtual station and publishes data via MQTT
display.py	Fetches and displays the latest sensor readings from ThingSpeak
venv/	Python virtual environment (not pushed to GitHub)

🔧 Technologies Used
Python 3.13
paho-mqtt for MQTT protocol
ThingSpeak (MathWorks cloud)
VS Code

How to Run
1. Setup Virtual Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # if you create one

2. Run the Sensor Publisher
python3 sensor.py

3. Run the Display Script
python3 display.py
